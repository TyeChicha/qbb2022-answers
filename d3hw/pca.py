#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt


# comp=np.genfromtxt("plink.eigenvec", dtype= None, encoding=None,names=["ID","ID2","PCA1","PCA2","PCA3"])
#
# fig, ax=plt.subplots(nrows=2)
#
# ax[0].scatter(comp["PCA1"],comp["PCA2"],label="PCA1:2")
# ax[1].scatter(comp["PCA1"],comp["PCA3"],label="PCA1:3")
#
# ax[0].legend()
# ax[0].set_xlabel("PCA1")
# ax[0].set_ylabel("PCA2")
#
# ax[1].legend()
# ax[1].set_xlabel("PCA1")
# ax[1].set_ylabel("PCA3")
#
# plt.savefig("ex2pca.png")

# colormf={"male":"blue","female":"red"}
# comp=np.genfromtxt(sys.argv[1], dtype= None, encoding=None,names=["ID","pop","spop","sex","ID","PCA1","PCA2","PCA3"])
# fig, ax=plt.subplots()
# ax.scatter(comp["PCA1"],comp["PCA2"],label="PCA1:2",c=colormf)
# ax.legend()
# ax.set_xlabel("PCA1")
# ax.set_ylabel("PCA2")
def visualize_color_2(data, qualities):                   #function to include
    # how I would do it with numpy
    plt.title('Numpy PCA {}'.format(qualities))               #title plot
    meta = np.unique(data[qualities])                             #gather list of uniq qualities of choice           
    for m in meta:                                                     #for qualities in my list of qualities, save index of lines
        indices = np.where(data[qualities]==m)[0]                      #with this quality and add these lines to scatterplot
        plt.scatter(data[indices]['PC1'], data[indices]['PC2'],label=m,alpha=.2,s=3)
    plt.legend(ncol=3, bbox_to_anchor=(.5,.4))                 #make legend
    plt.savefig('{}_PCA_numpy.png'.format(qualities))             #save fig
    plt.show()                                                     #show fig

if __name__ == "__main__":
    data = np.genfromtxt(sys.argv[1],                            #generate np array
                         dtype=None, encoding='UTF-8',
                         names=['sample_n1','pop','super_pop',
                                'gender','sample_n2','PC1','PC2','PC3'])
    for qual in ['pop','super_pop','gender']:               #for each variable i want color stratification by, run color function
        #visualize_color(data,qual)
        visualize_color_2(data,qual)

plt.show()
