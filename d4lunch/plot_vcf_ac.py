#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )
ac=log(ac)
fig, ax = plt.subplots()
ax.hist( ac, bins=100, density=True )
ax.set_xscale('log', base=10)
ax.set_xlabel("alt allele count")
ax.set_ylabel("frequency")
ax.set_xticks([0.01,0.1,1,10,100,1000])

title=vcf.split(".")[0]

ax.set_title("allele count frequencies of "+ title)
fig.savefig( title + ".png" )

fs.close()

