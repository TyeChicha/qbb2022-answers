medaka_variant -i methylation.bam -s r941_prom_snp_g360 -m r941_prom_variant_g360 -f hg38.fa -p -r ${x#*:} -o med${x%*:}

chr11:1900000-2800000 chr14:100700000-100990000 chr15:23600000-25900000 chr20:58800000-58912000

${x#*:} drops before colon
${x%*:} keeps before colon
1.
for x in chr11:1900000-2800000 chr14:100700000-100990000 chr15:23600000-25900000 chr20:58800000-58912000;do medaka_variant -i methylation.bam -s r941_prom_snp_g360 -m r941_prom_variant_g360 -f hg38.fa -p -r ${x} -o med${x%*:};done


2.
whatshap haplotag -o haplotagged.bam --reference reference.fasta phased.vcf.gz alignments.bam

whatshap haplotag -o chr11_hap.bam --reference hg38.fa --regions chr11:1900000:2800000 --output-haplotag-list chr11_tags.txt medchr11\:1900000-2800000/round_0_hap_mixed_phased.vcf.gz methylation.bam
whatshap haplotag -o chr14_hap.bam --reference hg38.fa --regions chr14:100700000:100990000 --output-haplotag-list chr14_tags.txt medchr14\:100700000-100990000/round_0_hap_mixed_phased.vcf.gz methylation.bam
whatshap haplotag -o chr15_hap.bam --reference hg38.fa --regions chr15:23600000:25900000 --output-haplotag-list chr15_tags.txt medchr15\:23600000-25900000/round_0_hap_mixed_phased.vcf.gz methylation.bam
whatshap haplotag -o chr20_hap.bam --reference hg38.fa --regions chr20:58800000:58912000 --output-haplotag-list chr20_tags.txt medchr20\:58800000-58912000/round_0_hap_mixed_phased.vcf.gz methylation.bam

3.
for x in chr11 chr14 chr15 chr20; do whatshap split --output-h1 h1$x --output-h2 h2$x ${x}_hap.bam ${x}_tags* ; done

samtools cat -o h1.bam h1*
samtools cat -o h2.bam h2*
]samtools index h1.bam 
]samtools index h2.bam 

