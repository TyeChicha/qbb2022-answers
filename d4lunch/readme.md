1a. output specifying bp covered
```
*** Subsetting .vcf for each feature
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp
```
1b.
you could try setting them == to eachother and seeing if it returns true or you could print 
the elements within the png files and see if those are equivaalent. also you could just look.

1c.
`cut -f9 gencode.v41.annotation.gtf | cut -f2 -d";" | grep "gene" | sort | uniq | less -S`
translated and untranslated processed pseudogenes because if translated they must produce proteins
mrna because they produce functional proteins

2a.
