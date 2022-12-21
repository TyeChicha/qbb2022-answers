#!/usr/bin/env python
# This code will make a PCA Plot from an eigenvec.
# arg1 = eigenvec
import sys
import numpy as np
import matplotlib.pyplot as plt
#part2
# cin=open(sys.argv[1])
# comp=np.genfromtxt(cin, dtype= None,                encoding=None,names=["ID","ID2","PCA1","PCA2","PCA3"])          #use eigenvec to generate pca plot

# fig, ax=plt.subplots()
#
# ax.scatter(comp["PCA1"],comp["PCA2"],label="PCA1:2")
#
# ax.legend()
# ax.set_xlabel("PCA1")
# ax.set_ylabel("PCA2")
# #plt.show()
# plt.savefig("pca12.png")

#part3
# cin2=open(sys.argv[2])             #turn .frq into list of strings
# fdata=[]
# for x,line in enumerate(cin2):
#     if x==0:
#         continue
#     hold=line.split()
#     fdata.append(hold[0]+' '+hold[1]+' '+hold[2]+' '+hold[3]+' '+hold[4]+' '+hold[5])
#
#
# fdata2=np.genfromtxt(fdata, dtype=None, encoding=None,       names=['CHR','ID','A1','A2','MAF','NCHROBS'])     #use genfromtxt to make np aarray of list of strings

# fig2,ax2= plt.subplots()
# plt.hist(fdata2['MAF'],label="Minor Allele Freqs")  # make plot of frequencies
# plt.savefig("frequencies.png")

#part5?
# assocfile=sys.argv[3]
# pval=np.genfromtxt(assocfile,names=True, dtype=None, encoding=None)
# fig,ax=plt.subplots()
# ax.scatter(pval['BP'],-np.log10(pval['P']))
# subset=pval[-np.log10(pval['P'])>5]
# ax.scatter(subset['BP'],-np.log10(subset['P']),color="red")
# plt.savefig('GSgwas.png')
# plt.show()
#
# assocfile=sys.argv[4]
# pval=np.genfromtxt(assocfile,names=True, dtype=None, encoding=None)
# fig2,ax2=plt.subplots()
# ax2.scatter(pval['BP'],-np.log10(pval['P']))
# subset2=pval[-np.log10(pval['P'])>5]
# ax2.scatter(subset2['BP'],-np.log10(subset2['P']),color="red")
#
# plt.savefig('CBgwas.png')
# plt.show()

# part6
#bash arguments
#grep rs269622 genotypes.vcf | sed 's/\t/\n/g' | grep / > gene.txt
#sed 's/\t/_/' GS451_IC50.txt >phen.txt

phen=np.genfromtxt(sys.argv[5],names=True,dtype=None,encoding=None)
geno=np.genfromtxt(sys.argv[6],names='allele',dtype=None,encoding=None)

alt=[]
het=[]
ref=[]

for x in range(len(phen)):
    if phen[x][1]=='NA':
        continue
    if geno[x][0]=='0/0':
        ref.append(float(phen[x][1]))
    elif geno[x][0]=='1/0' or geno[x][0]=='0/1':
        het.append(float(phen[x][1]))
    elif geno[x][0]=='1/1':
        alt.append(float(phen[x][1]))
    else:
        pass

fig,ax=plt.subplots()
ax.set_ylabel('IC50')
ax.set_xlabel('genotype')
ax.set_xticklabels(labels=['0/0','1/0 or 0/1', '1/1'])
plt.title('SNP:rs269622 effect size')
ax.boxplot([ref,het,alt])
plt.savefig('effectsize.png')
plt.show()