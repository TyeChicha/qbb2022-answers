Part 1.
{
	Step 1
	for x in *.bam; do samtools view -q 10 -o f$x $x;done
	
	step 2
	565  macs2 callpeak -t fD2_Sox2_R1.bam -c fD2_Sox2_R1_input.bam -f BAM -g 8.3e7 -B --outdir R1peakcalls
	566  macs2 callpeak -t fD2_Sox2_R2.bam -c fD2_Sox2_R2_input.bam -f BAM -g 8.3e7 -B --outdir R2peakcalls
	
	step 3
	bedtools intersect -a R1peakcalls/NA_peaks.narrowPeak -b R2peakcalls/NA_peaks.narrowPeak -wa > interpeaks.bed
	
	step 4 
    588  bedtools intersect -a interpeaks.bed -b D2_Klf4_peaks.bed -wa
    589  bedtools intersect -a interpeaks.bed -b D2_Klf4_peaks.bed -wa | wc -l
	42/582

	step 5
	for x in *.bdg; do python scale_bdg.py $x scaled$x; done
	for x in scaled*; do awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' $x > crop_$x; done
	plot.py file1-4
}
part 2 
sort -k5 -n -r interpeaks.bed | head -n 300 | awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' > cinterpeaks.narrowpeaks
samtools faidx -r cinterpeaks.narrowpeaks mm10.fa -o seqsox.fa
meme-chip -maxw 7 -db mm10.fa seqsox.fa -o motif

part3
 558  tomtom motif/combined.meme motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme 
  559  man open
  560  open -a safari tomtom_out/tomtom.html 
  561  less -S tomtom_out/tomtom.tsv 
  562  man grep
  563  grep "KLF4" tomtom_out/tomtom.tsv 
  564  grep "KLF4" tomtom_out/tomtom.tsv > matches.tsv
  565  grep "SOX2" tomtom_out/tomtom.tsv 
  566  grep "SOX2" tomtom_out/tomtom.tsv >>matches.tsv 


