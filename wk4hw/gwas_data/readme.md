2.
plink --vcf genotypes.vcf --double-id --make-bed --pca --out pcafiles
#to generate pca
#used plot.py to generate plot with command
./plot.py pltdata.eigenvec     

3.plink --vcf genotypes.vcf --freq
./plot.py pltdata.eigenvec plink.frq
#see plot.py and frequency.png

4.  
plink --vcf genotypes.vcf --assoc --linear --pheno GS451_IC50.txt --covar pcafiles.eigenvec --allow-no-sex --out GSphenotyperesults
plink --vcf genotypes.vcf --assoc --linear --pheno CB1908_IC50.txt --covar pcafiles.eigenvec --allow-no-sex --out CBphenotyperesults

5. 
#joint not workin frfr. takes infinite time generating figure.
assocfile=sys.argv[3]
pval=np.genfromtxt(assocfile,names=True, dtype=None, encoding=None)
print(pval)
fig,ax=plt.subplots()
ax.scatter(pval['SNP'],pval['P'])
plt.show()
#this generates nothing and gets stuck in something forever but theres no loop to get stuck in.
#finally generated figs... ran for like 30mins...
#GSgwas.png and CBgwas.png
./plot.py pltdata.eigenvec plink.frq GSphenotyperesults.qassoc CBphenotyperesults.qassoc 

6.GS  rs269622   p=0.0001018


