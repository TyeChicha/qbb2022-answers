#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.text as txt
import sys


#starting allel freq (p) and pop size (n) as input
#n is number of organisms, so use 2n in sim for number of chr
#part 1 function
def allelesim(p,n):
    afreqs=[]
    afreqs.append(p)
    while (p != 0) and (p!=1):
        p=(np.random.binomial(2*n,p))/(2*n)
        afreqs.append(p)
    return(afreqs)
    
def main():
    # #part2
#     sim=allelesim(0.5,100)
#     print(sim)
#     gen=list(range(len(sim)))
#     print(gen)
#     fig,ax=plt.subplots()
#     ax.plot(gen,sim)
#     plt.xlabel('generation')
#     plt.ylabel('allele frequency')
#     plt.ylim(0,1)
#     ax.text(s='Starting p=0.5',x=0,y=1)
#     plt.savefig('part2.png')
#     plt.show()
#     plt.close()
    
    #part3
     fig,ax=plt.subplots()
     plt.xlabel('set time')
     plt.ylabel('freq')
     ax.text(s='Starting p=0.5',x=0,y=1)
     simgens=[]
     for i in range(1000):
         sim=allelesim(0.5,100)
         gen=len(sim)
         simgens.append(gen)
     print(simgens)
     ax.hist(simgens,bins=100)
     plt.savefig('part3.png')
     plt.show()
     plt.close()
    
    #part4 sims with varying pop size
    # popsize=[]
#     fixtime=[]
#     for i in [100,1000,10000,100000,1000000,10000000]:
#         sim=allelesim(0.5,i)
#         popsize.append(i)
#         fixtime.append(len(sim))
#     fig,ax=plt.subplots()
#     ax.plot(popsize,fixtime)
#     plt.xlabel('pop size')
#     plt.ylabel('fix time')
#     plt.xticks(ticks=popsize)
#     plt.xscale('log')
#     plt.yscale('log')
#     plt.savefig('part4.png')
#     plt.show()
#     plt.close()
#

#part 5 sims with varying allele frequency + violin plot
    # allelefreq=[0.09,0.18,0.27,0.36,0.45,0.54,0.63,0.72,0.81,0.90]
#     fig,ax=plt.subplots()
#     plt.xlabel('allele startings freq')
#     plt.ylabel('fix time')
#     plt.ylim(0,1500)
#     ax.text(s='Population size: 100',x=0,y=1500)
#     settimes=np.zeros((100,len(allelefreq)))
#     for x in range(settimes.shape[1]):
#         for y in range(settimes.shape[0]):
#             settimes[y][x]=len(allelesim(allelefreq[x],100))
#     ax.violinplot(settimes,positions=[1,2,3,4,5,6,7,8,9,10],showextrema=False,showmeans=True,widths=0.8)
#     plt.xticks(ticks=[1,2,3,4,5,6,7,8,9,10],labels=allelefreq)
#     plt.savefig('part5.png')
#     plt.show()

     
if __name__ == '__main__':
    main()
    
    