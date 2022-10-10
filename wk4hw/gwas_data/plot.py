#!/usr/bin/env python
# This code will make a PCA Plot from an eigenvec.
# arg1 = eigenvec
import sys
import numpy as np
import matplotlib.pyplot as plt
#part2
# cin=open(sys.argv[1])
# comp=np.genfromtxt(cin, dtype= None,                encoding=None,names=["ID","ID2","PCA1","PCA2","PCA3"])          #use eigenvec to generate pca plot
#
# fig, ax=plt.subplots()
#
# ax.scatter(comp["PCA1"],comp["PCA2"],label="PCA1:2")
#
# ax.legend()
# ax.set_xlabel("PCA1")
# ax.set_ylabel("PCA2")
# #plt.show()
# plt.savefig("pca12.png")
#
# #part3
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
#
# fig2,ax2= plt.subplots()
# plt.hist(fdata2['MAF'],label="Minor Allele Freqs")  # make plot of frequencies
# plt.savefig("frequencies.png")

# #part5?
# assocfile=sys.argv[3]
# pval=np.genfromtxt(assocfile,names=True, dtype=None, encoding=None)
# print(pval)
# fig,ax=plt.subplots()
# ax.scatter(pval['SNP'],-np.log10(pval['P']))
# plt.savefig('GSgwas.png')
#
# assocfile=sys.argv[4]
# pval=np.genfromtxt(assocfile,names=True, dtype=None, encoding=None)
# print(pval)
# fig2,ax2=plt.subplots()
# ax2.scatter(pval['SNP'],-np.log10(pval['P']))
# plt.savefig('CBgwas.png')

#part6
phen=sys.argv[1]
geno=sys.argv[2]
