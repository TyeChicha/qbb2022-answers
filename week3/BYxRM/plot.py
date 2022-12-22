#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np
from vcf_parser_2 import parse_vcf

vcf=parse_vcf(sys.argv[1])
#print(vcf[0].split(',')[7])

depth=[]
qual=[]
af=[]
effect=[]

#print(vcf[0])
for i,x in enumerate(vcf):
    y=x
    af.append(y[7]['AF'])
    effect.append(y[7]['ANN'].split('|')[1])
    for j in range(9,19):
        if y[j][1]!='.':qual.append(y[j][1])
        if y[j][2]!='.':depth.append(y[j][2]) 
        
# for item in depth:item=int(item)
# for item in qual:item=float(item)
depth=[int(num) for num in depth]
qual=[float(num) for num in qual]
af2=[]
for num in af:
    try:
        hold=float(num)
        af2.append(hold)
    except:
        pass
effect=[x for x in effect if x]
effectx, effecty = np.unique(np.array(effect), return_counts = True)
effectx=[x.split('&')[0] for x in effectx]
#print(af2)
#print(effect)
#print(qual)
#print(depth)

#some plots
fig,ax=plt.subplots(nrows=2,ncols=2)

ax[0][0].hist(depth,bins=200)
ax[0][0].set_xlim(xmin=0,xmax=800)
ax[0][0].set_yscale('log')
ax[0][0].set_ylabel('freq')
ax[0][0].set_xlabel('Depth of Reads')
ax[0][0].set_title('Read Depth Distribution')

ax[0][1].hist(qual,bins=40)
ax[0][1].set_xlim(xmin=0,xmax=160)
ax[0][1].set_yscale('log')
ax[0][1].set_ylim(ymin=1000,ymax=100000)
ax[0][1].set_ylabel('freq')
ax[0][1].set_xlabel('Qual Score')
ax[0][1].set_title('Read Quality Distribution')

ax[1][0].hist(af2,bins=20)
ax[1][0].set_xlim(xmin=0,xmax=1)
ax[1][0].set_xticks([0.0,0.2,0.4,0.6,0.8,1.0])
ax[1][0].set_ylabel('freq')
ax[1][0].set_yscale('log')
ax[1][0].set_xlabel('AlleleFreq')
ax[1][0].set_title('Allele Freq. Distribution')

plt.xticks(rotation=45, ha='right',fontsize='xx-small')
ax[1][1].bar(effectx,effecty,log=True)
ax[1][1].set_ylabel('freq')
ax[1][1].set_xlabel('Predicted Effect')
ax[1][1].set_title('Effect Distribution')

plt.tight_layout()
plt.savefig('THEEfig.png')
plt.show()