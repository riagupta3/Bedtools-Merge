#!/usr/bin/python3
import json
import os
import subprocess
import sys

# Need Auxillary functions section?
# currently not using createTag?
def createTag(inputJson, tag, manifestName):
    parameterString = ""
    if inputJson.get(manifestName):
        parameterString = " -" + tag + " "
    return parameterString

# Parse input json
with open("/batchx/input/input.json", "r") as inputFile:
    inputJson = inputFile.read()
parsedJson = json.loads(inputJson)

# BX_MEMORY & BX_VCPUS - don't need
bxMemory = os.environ['BX_MEMORY']
bxVcpus = os.environ['BX_VCPUS']

# intervalFile
intervalFile = parsedJson["intervalFile"]

# Optional inputs
optString = ""

# -s
if "strandedness" in parsedJson:
    s = parsedJson["strandedness"]
    if s is False:
        sString = ""
    elif s is True:
        sString = "-s "
    optString += sString
 
# choose between two implementations - this might return strandedness instead of "s"
optString += createTag(parsedJson, "s", "strandedness")

# -S
# should spaces be before or after the parameter
if "specificStrand" in parsedJson:
    S = parsedJson["specificStrand"]
    if S.lower() == "forward":
        SString = "-S + "
    elif S.lower() == "reverse":
        SString = "-S - "
    optString += SString

# -d
if "distance" in parsedJson:
    d = parsedJson["distance"]
    optString += "-d " + d + " "
    
# -c and -o
if "operator" in parsedJson:
    c = parsedJson["columns"]
    operatorString = createTag(parsedJson, "c", "columns") + c + " "
    o = parsedJson["operation"]
    operatorString += createTag(parsedJson, "o", "operation") + o + " "
    optString += operatorString

    
# -header
optString += createTag(parsedJson, "header", "header")

# -delim
if "delimiter" in parsedJson:
    delim = parsedJson["delimiter"]
    optString += createTag(parsedJson, "delim", "delimiter") + delim + " "
    
# define output dir
outputDir = "/batchx/output/"

outputDir += "bedtools-merge/"
os.mkdir(outputDir)

# outputPrefix
outputPrefix = "merged"
if "outputPrefix" in parsedJson:
    outputPrefix = parsedJson["outputPrefix"]
    
# mergedFile
# change .bed depending on output file type when running the tool
mergedFile = outputDir + outputPrefix + ".bed"

try:
    bedtoolsVersionCmd = "bedtools -version"
    subprocess.check_call (bedtoolsVersionCmd, shell=True)
    cmmd = "bedtools merge"\
        + "-i " + intervalFile\
        + optString\
        # would this line be the same or modified
        + " 3>&1 1>&2 2>&3 >" + mergedFile + "| tee -a /batchx/output/log.txt"
    print(cmmd, flush=True)
    subprocess.check_call (cmmd, shell=True)

except subprocess.CalledProcessError as e:
        print(e)
        exit(e.returncode)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

exitCode = 0
grepSkipping = subprocess.call(["grep","Skipping.","/batchx/output/log.txt"],stdout=False)
if grepSkipping==0:
    exitCode = 7
    
# Write output json file
outputJson = {
    'mergedFile': mergedFile
}
with open('/batchx/output/output.json', 'w+') as json_file:
    json.dump(outputJson, json_file)
    
