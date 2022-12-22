#!/usr/bin/env python

import scanpy as sc
import sys
import matplotlib.pyplot as plt



#read data in
data=sc.read_10x_h5(sys.argv[1])

# make unique variable names?
data.var_names_make_unique()

print(data)
#step1 filter
#pre pca
fig, ax= plt.subplots()
sc.tl.pca(data)
sc.pl.pca(data,show=False,ax=ax)
plt.savefig('prepca.png')
plt.show()
plt.close()

#filter?
sc.pp.recipe_zheng17(data)

#post filter pca
fig, ax= plt.subplots()
sc.tl.pca(data)
sc.pl.pca(data,show=False,ax=ax)
plt.savefig('postpca.png')
plt.show()
plt.close()

#step2 cluster

sc.pp.neighbors(data)
sc.tl.leiden(data)

sc.tl.tsne(data)
sc.pl.tsne(data,show=True,save='tsne.png')
sc.tl.umap(data,maxiter=1000)
sc.pl.umap(data,show=True,save='umap.png')

#step3
#ttest
sc.tl.rank_genes_groups(data,groupby='leiden',method='t-test')
sc.pl.rank_genes_groups(data,show=True,save='ttest.png')
#regression
sc.tl.rank_genes_groups(data,groupby='leiden',method='logreg')
sc.pl.rank_genes_groups(data,show=True,save='regression.png')

#step4?
