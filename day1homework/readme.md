<<<<<<< Local Changes
<<<<<<< Local Changes
# QBB2022 - Day 1 - Homework Exercises Submission
1.

redeclare nuc inside of awk.=======
=======
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
358 A
1317 C
<<<<<<< Local Changes
386 G

yes because pyrimidines tend to swap for pyrimidines and same for purines

2.

awk '{if ($4 == "2") {print}}' ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > promos.bed
#gives list of state 2 (promoter like shit)
#promoters not clearly defined. closest is state 2 which is TSS flanking regions
bedtools intersect -a ~/data/vcf_files/random_snippet.vcf -b promos.bed | ex2.sh
ex2{
for nuc in C
do
  echo "Considering " $nuc
  awk -v nuc=$nuc '/^#/{next} {if ($4 == nuc) {print $5}}' $1 | sort | uniq -c
done
}
#gives intersecting variants and variants based on ref C


=======
Considering  C
   7 A
   4 G
  24 T

C is most often replaced by T likely due to their relation and high occurence of T rather than C in promoter regions

3.
awk -v OFS='\t' '/^#/{next} {print $1,/t,$2-1,/t, $2}' $1 > variants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.bed -b genes.sorted.bed

~51.5 variants per gene


4. 

bedtools intersect -a ~/data/bed_files/H3K27ac.naive_b_cell.GRCh38.bedgraph -b ~/data/bed_files/genes.bed -wb | cut -f8 | sort | uniq > genes_intersecting_H3K27ac_b_cell.txt

bedtools intersect -a ~/data/bed_files/H3K9me3.naive_b_cell.GRCh38.bedgraph -b ~/data/bed_files/genes.bed -wb | cut -f8 | sort | uniq > genes_intersecting_H3K9me3_b_cell.txt

grep -vf genes_intersecting_H3K9me3_b_cell.txt genes_intersecting_H3K27ac_b_cell.txt

needed to include full path and the swap file order for final step and -v must come before -f


