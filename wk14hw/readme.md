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
#3D: you could blast each contig against prokaryotes database and compare the size to the known genome and figure out what contigs dont belong

#step3 
#from bins_dir
for x in *.fa; do grep ">" $x > ${x}.list1; done;
for x in *.list1; do j=`basename $x .list1`; cat $x | while read line; do echo ${line:1} >> ${j}.list2; done; done;
for x in *.list2; do j=`basename $x .fa.list2`; cat $x | while read line; do grep ${line} ../../KRAKEN/assembly.kraken >> ${j}.txt; done; done;
for x in *.txt; do echo $x; for y in 7 9 11; do echo column $y; cut -f$y -d";" $x | sort | uniq -c; done; done
#output from above
bin.1.txt
column 7
  77 Bacillales
column 9
  77 Staphylococcus
column 11
   2
  24 Staphylococcus epidermidis ATCC 12228
  51 Staphylococcus epidermidis RP62A
bin.2.txt
column 7
  38 Bacillales
column 9
  38 Staphylococcus
column 11
   2
   1 Staphylococcus aureus CA-347
   6 Staphylococcus aureus subsp. aureus
   3 Staphylococcus epidermidis ATCC 12228
   2 Staphylococcus epidermidis RP62A
  24 Staphylococcus haemolyticus JCSC1435
bin.3.txt
column 7
  53 Bacillales
column 9
  53 Staphylococcus
column 11
  53 Staphylococcus aureus subsp. aureus
bin.4.txt
column 7
  12 Propionibacteriales
column 9
  12 Cutibacterium
column 11
  12 Cutibacterium avidum 44067
bin.5.txt
column 7
   2 Clostridiales
   1 Lactobacillales
   5 Tissierellales
column 9
   3 Anaerococcus
   2 Clostridium
   2 Finegoldia
   1 Streptococcus
column 11
   1
   3 Anaerococcus prevotii DSM 20548
   1 Clostridium novyi NT
   2 Finegoldia magna ATCC 29328
   1 Streptococcus anginosus
bin.6.txt
column 7
   6 Lactobacillales
column 9
   6 Enterococcus
column 11
   1 Enterococcus faecalis D32
   2 Enterococcus faecalis OG1RF
   2 Enterococcus faecalis V583
   1 Enterococcus faecalis str. Symbioflor 1
#question 4A: i predict these will only be variation at the species level in each bin due to their being sorted into the bins based on taxonomy already
#question 4B: perform statistical test of the probability of each taxonomic level being present at its ratio within the bin versus in equal portions and that should tell you the whether it is safe to assume the bin is that classification

git add readme.md metagenomics_data/step0_givendata/KRAKEN/*.html 