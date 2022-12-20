#!/usr/bin/env python

#step 1
#for x in SRR*; do sed 's/;/\t/g' $x | cut -f2-11 > ${x}_krona.txt; done
#my version of the conversion

#for i in *.txt; do j=`basename $i .kraken_krona.txt`; ktImportText -q $i -o "${j}.html"; done

#1 there is a marked decrease in cutibacteria that does recovers strongly by the end of the week. Staph shows a much less drastic drop and recovery.

#step2
bwa index assembly.fasta 
for x in *1.fastq; do j=`basename $x _1.fastq`; bwa mem ../assembly.fasta ${j}_1.fastq ${j}_2.fastq > ${j}.sam; done

for x in *.sam; do j=`basename $x .sam`;samtools sort -O sam $x > ${j}_sorted.sam; done

#3A: 6 bins (13170431 bases in total) formed.
#3B: roughly 4.7% of assembly
for x in bin*; do echo $x; grep ">" $x | wc -l; done
# bin.1.fa
#       77
# bin.2.fa
#       38
# bin.3.fa
#       53
# bin.4.fa
#       12
# bin.5.fa
#        8
# bin.6.fa
#        6
grep ">" ../assembly.fasta | wc -l
#   4103
#3C: i dont think they are all right because there range is quite large, from 6 - 77 contigs
#3D: you could blast each contig against prokaryotes database 
