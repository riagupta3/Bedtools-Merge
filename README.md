# Bedtools-Merge
Combines overlapping or book-ended features in a BED/GFF/VCF/BAM interval file into a single feature which spans all of the combined features using the bedtools [merge](https://bedtools.readthedocs.io/en/latest/content/tools/merge.html) function.

# Context

This tool combines features with overlapping or book-ended intervals into a single feature. This interval file can be of the following type:

1. [BED (Browser Extensible Data)](https://genome.ucsc.edu/FAQ/FAQformat.html#format1)
2. [GFF (General Feature Format)](https://genome.ucsc.edu/FAQ/FAQformat.html#format3)
3. [VCF (Gene Transfer Format) ](https://genome.ucsc.edu/goldenPath/help/vcf.html)
4. [BAM (binary version of the SAM (Sequence Alignment/Map) format)](https://genome.ucsc.edu/goldenPath/help/bam.html)

# Inputs

## Required inputs

This tool has the following **required** inputs:

1. **`intervalFile`**
  
  BED/GFF/VCF/BAM interval file. File containing multiple overlapping or book-ended regions to be merged. 

## Optional inputs

This tool provides additional configuration through the following **optional** inputs:

1. **`strandedness`**

  Force strandedness by only merging features on the same strand. This feature is disabled by default (default: `false`).

2. **`specificStrand`**
  
  Force merge for one specific strand only. Follow with a + or - to force merge from only the forward or reverse strand, respectively. Merging is done without respect to strand, by default.

3. **`distance`**

  The maximum distance between features allowed for features to be merged. The default is to merge overlapping and/or book-ended features (default: `0`).

4.  **`operator`**
    
    Specify the operation to be used and the columns to be operated upon. 
    
    a. **`columns`**
      
    Specify columns from the input file to be operated upon. A comma-delimited list can be used to specify multiple columns.
    
    This is a *required* input if using the **`operator`** input.
    
    b. **`operation`**
    
    Specify the operation that should applied to columns. A comma-delimited list can be used to specify multiple operations. If there is only one column,
    but multiple operations, all operations will be applied on that column. If there is only one operation specified, but multiple columns, that operation
    will be applied to all columns. Otherwise, the number of columns must match the the number of operations, and will be applied in respective order.
    
    Valid operations are: sum, min, max, absmin, absmax, mean, median, collapse (i.e., print a delimited list (duplicates allowed)), distinct (i.e., print 
    a delimited list (NO duplicates allowed)), count, count_distinct (i.e., a count of the unique values in the column). The default operation is `sum`.
    
    This is an *optional* input (default: `sum`).

5. **`header`**

  Print the header from the interval file prior to results.

6. **`delim`**

  Specify a custom delimiter (default: `,`).

7. **`outputPrefix`**

  Prefix name for the output file (default: `merged`).

# Outputs

## Required outputs

This tool will **always** provide the following output:

1. **`mergedFile`**

  BED file containing the combined features.

# Example

## Get input data

Copy the contents below and save them to a file as `test.bed`.

```shell
chr1	100	200
chr1	180	250
chr1	250	500
chr1	501	1000
```

## Upload input data into BatchX

Use the following command to upload this file into your BatchX file system:

```shell
bx cp test.bed bx://test/bedtools/merge/
```

## Submit job

Submit a job to merge the overlapping/book-ended features contained in the interval file (`test.bed`).

```shell
bx submit batchx@
```

This job generates a BED file with the content shown below:

```shell
chr1	100	500
chr1	501	1000
```

# Links

* [bedtools manual](https://bedtools.readthedocs.io/en/latest/index.html)
* [bedtools merge documentation](https://bedtools.readthedocs.io/en/latest/content/tools/merge.html)
* [Bioinformatics file formats](https://genome.ucsc.edu/FAQ/FAQformat.html)
* [bedtools Github repository](https://github.com/arq5x/bedtools2)


