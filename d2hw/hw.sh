#!/usr/bin/env python3
#usage script [file1, file2]
from vcfParser import parse_vcf
import sys

vcf=parse_vcf(sys.argv[1])            #holder variable for parsed file1
fin2=open(sys.argv[2])               #set filestream for file2
dic={}                              #initialize dictionary for key=chrom,pos  value= ID
for line in fin2:                    #for each line of file2
    if line.startswith('#'):            #skip if a header
        continue
    hold=line.split('\t')           #split line by tab
    key=(hold[0],hold[1])               #temp key holder for chrom and pos
    dic.setdefault(key,hold[2])            #add key and ID to dictionary
count=0                              #iinitialze no ID count
for i,x in enumerate(vcf):               #for lines from file 1 (went through parser)
    if i == 0:                        #skip first line
        continue
    if (x[0],str(x[1])) in dic:             #if chrom ann position present in dictionary, fill ID in with dictionary value
        x[2]=dic[(x[0],str(x[1]))] 
        vcf[i][2] = x[2]
    else:                             #if not add 1 to no ID count
        count+=1
    
print("variants without ID: " + str(count))


