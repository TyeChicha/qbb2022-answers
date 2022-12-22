#!/usr/bin/env python

# step1: index
bwa index sacCer3.fa 
# step2: align with bwa mem
for x in *; do j=`basename $x .fastq`; bwa mem -R "@RG\tID:$j\tSM:$j" -t 5 ../sacCer3.fa $x > ${j}.sam; done
# step3:create sorted bam files with samtools and  index them
for x in *.sam; do j=`basename $x .sam`; samtools sort -o sorted_$j.bam -O bam $x; samtools index -b sorted_$j.bam sorted_$j.bam.bai; done
# step4: variant calling
freebayes -f ../sacCer3.fa --genotype-qualities -p 1 *.bam > yeast.vcf
# step5 + 6: fillter variantr with vcffilter & dexompose haplotypes with vcfallelicprimitives
vcffilter -f "QUAL > 20" yeast.vcf | vcfallelicprimitives -k -g > sacCer3.vcf
# step7: variant effect predict with snpeff ann
snpeff ann R64-1-1.99 sacCer3.vcf > sacCer3.effectpredict.vcf
# step8:  analysis