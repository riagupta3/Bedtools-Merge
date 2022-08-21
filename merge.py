#!/usr/bin/python3
import json
import os
import subprocess
import sys
from Bio import SeqIO

# Need Auxillary functions section?

# Parse input json
with open("/batchx/input/input.json", "r") as inputFile:
    inputJson = inputFile.read()
parsedJson = json.loads(inputJson)

# BX_MEMORY & BX_VCPUS
bxMemory = os.environ['BX_MEMORY']
bxVcpus = os.environ['BX_VCPUS']

# intervalFile
intervalFile = parsedJson["intervalFile"]

# need section that follows in getfasta file?

