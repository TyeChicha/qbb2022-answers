# QBB2022 repository
#QBB2022 - Day 1 - Lunch Exercises Submission

1. im excited to learn python eventually.

2. 
wc -l exons.chr21.bed
wc -l exons.chr21.bed
13653/219= 62.34
Map exons to genes and make a list of numbers of exons for each gene
sort list and use head -half the number of genes
 to find middle one

3.
echo cut -f4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort -n | uniq -c -d >> README.md

 305 1
 678 2
  79 3
 377 4
 808 5
 148 6
1050 7
 156 8
 654 9
  17 10
  17 11
  30 12
  62 13
 228 14
 992 15
<<<<<<< Local Changes
 
 script to identify state then subtract column 2 from 3 to get distance and add to total distance for that state. this would count total for each state.
 
 4.
 grep "AFR" integrated_call_samples.panel | cut -f2 | sort | uniq -c
 
 
=======
 123 ACB
 112 ASW
 173 ESN
 180 GWD
 122 LWK
 128 MSL
 206 YRI
>>>>>>> External Changes

use sort | uniq to make list of superpopulations then make a loop of previous command utilizing superpop list

5.
9514 0|0
 127 0|1
 178 1|0
 181 1|1
<<<<<<< Local Changes
 
 34 lines contain AF=1
 15 lines contain ;AF=1;
 
 Max 6 occurences in a line
 
 use grep to search AFR=* and p
=======
  