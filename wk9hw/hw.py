#!/usr/bin/env python
import sys
import numpy as np
import numpy.lib.recfunctions as rfn
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import matplotlib.pyplot as plt
import seaborn as sns
import numpy.lib.recfunctions as rfn
import scipy
from scipy import stats
import statsmodels.formula.api as smf
import statsmodels.api as sm
import pylab
from statsmodels.stats import multitest


print(sys.getrecursionlimit())
sys.setrecursionlimit(100000)
#0a
fin = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')

col_names = list(fin.dtype.names)
col_names = col_names[1:]
row_names = fin['t_name']
#print(col_names)
#print(row_names)

input1d= fin[:][col_names]
#print(input1d)

#0b
input2d = rfn.structured_to_unstructured(input1d, dtype=np.float64)
median=np.median(input2d,axis=1)

subset=input2d[np.where(median > 0)[0]]
row_names=row_names[np.where(median > 0)[0]]
subset= np.log2(subset + 0.1)



#step 1
# linkmtx=linkage(subset, optimal_ordering=True)
# leaf=leaves_list(linkmtx)
# #plt.figure()
# dendrogram(linkmtx,p=10, truncate_mode='level')
# plt.savefig('dendro.png')
# fig, ax=plt.subplots()
# ax=sns.clustermap(subset, row_linkage=linkmtx, col_cluster=True, xticklabels=col_names, yticklabels=False)
# plt.savefig('heat.png')
# plt.show()


#step 2
pval = []
bval = []
pval2=[]
bval2=[]
#making array of data
sexes = ['male', 'male', 'male', 'male', 'male', 'female', 'female', 'female', 'female', 'female']
stages = ['10', '11', '12', '13', '14', '10', '11', '12', '13', '14']
for i in range(subset.shape[0]):
    list_of_tuples = []
    for j in range(len(col_names)):
        list_of_tuples.append((row_names[i],subset[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    #by stage regression
    regression = smf.ols(formula = 'fpkm ~ stage', data = longdf).fit()
    pvalue = regression.pvalues['stage']
    beta = regression.params['stage']
    pval.append(pvalue)
    bval.append(beta)
    #by stage and sex regression
    regression = smf.ols(formula = 'fpkm ~ stage + sex', data = longdf).fit()
    pvalue = regression.pvalues['stage']
    beta = regression.params['stage']
    pval2.append(pvalue)
    bval2.append(beta)

#by stage qq plot
fig,ax = plt.subplots()
sm.qqplot(np.array(pval),dist= scipy.stats.uniform, line= "45",ax=ax)
plt.savefig("stageqq.png")
plt.show()
plt.close()


    
    
#stage dif expression
correction= multitest.multipletests(pval, alpha=0.3, method = "fdr_bh")
rejection= correction[0]
#print(rejection)
sigrows=row_names[rejection]
print("differentially expressed transcripts (stage):")
print(sigrows)

#stage + sex dif expression
correction= multitest.multipletests(pval2, alpha=0.3, method = "fdr_bh")
rejection= correction[0]
sigrows2=row_names[rejection]
print("differentially expressed transcripts (stage + sex):")
print(sigrows2)

#overlapping dif expressed transcipts
overlap = set(sigrows) & set(sigrows2)
print("Overlapping transcripts:")
print(overlap)
print("percent overlap (stage) vs (stage + sex):")
print((len(overlap)/len(sigrows))*100)

#plot dif express (stage + sex)
fig,ax=plt.subplots()
colour=[]
for x in rejection:
    if x==True:
        colour.append('red')
    else:
        colour.append('black')
ax.scatter(bval2,-np.log10(pval2),color=colour)
plt.savefig('stagesexvolcano.png')
plt.show()
plt.close()


sys.setrecursionlimit(1000)


