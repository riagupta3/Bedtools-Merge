# Bedtools-Merge
Combines overlapping or book-ended features in a BED/GFF/VCF/BAM interval file into a single feature which spans all of the combined features using the bedtools [merge](https://bedtools.readthedocs.io/en/latest/content/tools/merge.html) function.

# Context

# Inputs

## Required inputs

This tool has the following **required** inputs:

1. **`i`**
  
  BED/GFF/VCF/BAM interval file. File containing multiple overlapping or book-ended regions to be merged. 

## Optional inputs

This tool provides additional configuration through the following **optional** inputs:

1. **`s`**

  Force strandedness by only merging features on the same strand. This feature is disabled by default (default: `false`).

2. **`S`**
  
  Force merge for one specific strand only. Follow with a + or - to force merge from only the forward or reverse strand, respectively. Merging is done without respect to strand, by default.

3. **`d`**

  The maximum distance between features allowed for features to be merged. The default is to merge overlapping and/or book-ended features (default: `0`).

4. **`c`**

  Specify columns from the input file to operate upon (see -o option). A comma-delimited list can be used to specify multiple columns. 

5. **`o`**

  Specify the operation that should applied to -c. A comma-delimited list can be used to specify multiple operations. If there is only one column, but multiple operations, all operations will be applied on that column. If there is only one operation specified, but multiple columns, that operation will   be  applied to all columns. Otherwise, the number of columns must match the the number of operations, and will be applied in respective order. 
  
  Valid operations are: sum, min, max, absmin, absmax, mean, median, collapse (i.e., print a delimited list (duplicates allowed)), distinct (i.e., print a delimited list (NO duplicates allowed)), count, count_distinct (i.e., a count of the unique values in the column). Default: `sum`.

6. **`header`**

  Print the header from the A file prior to results.

7. **`delim`**

  Specify a custom delimiter for the -nms and -scores concat options (default: `;`).

8. **`outputPrefix`**

  Prefix name for the output file (default: `merged`).

# Outputs

## Required outputs

This tool will **always** provide the following output:

1. **`mergedFile`**

  *add description*

# Example

## Get input data


