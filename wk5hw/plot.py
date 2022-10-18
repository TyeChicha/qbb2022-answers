#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt
from bdg_loader import load_data

f1=sys.argv[1]
f2=sys.argv[2]
f3=sys.argv[3]
f4=sys.argv[4]
d1=load_data(f1)
d2=load_data(f2)
d3=load_data(f3)
d4=load_data(f4)

fig,ax=plt.subplots(nrows=4)

ax[0].plot(d1['X'],d1['Y'])
ax[0].fill_between(d1['X'],d1['Y'])
ax[0].set_title(f1)
ax[0].set_ylim(ymin=0, ymax=20000)
ax[0].set_xlim(auto=True)

ax[1].plot(d2['X'],d2['Y'])
ax[1].fill_between(d2['X'],d2['Y'])
ax[1].set_title(f2)
ax[1].set_ylim(ymin=0, ymax=20000)
ax[1].set_xlim(auto=True)

ax[2].plot(d3['X'],d3['Y'])
ax[2].fill_between(d3['X'],d3['Y'])
ax[2].set_title(f3)
ax[2].set_ylim(ymin=0, ymax=20000)
ax[2].set_xlim(auto=True)

ax[3].plot(d4['X'],d4['Y'])
ax[3].fill_between(d4['X'],d4['Y'])
ax[3].set_title(f4)
ax[3].set_ylim(ymin=0, ymax=20000)
ax[3].set_xlim(auto=True)

plt.tight_layout()
plt.savefig('sixk.png')