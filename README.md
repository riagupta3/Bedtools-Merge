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

  The maximum distance between features allowed for features to be merged.

4. **`c`** 

# Outputs

## Required outputs

This tool will **always** provide the following output:
