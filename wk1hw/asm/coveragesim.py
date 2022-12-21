#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def coveragesim():                         #generate simulated coverage
    coverage=[0] * 1000000
    for i in range(150000):
        read=np.random.randint(0,999900)
        for j in range(read,read+100):
            coverage[j]+=1
    print(np.sum(coverage)/1000000)
    return(coverage)

x=np.array(coveragesim())         
y=np.where(x==0) 
print(len(y[0])/1000000)              
 #plot coverage and poisson dist of said coverage

fig,ax=plt.subplots()
ax.hist(x, label='coverage', density=True)
ax.plot(x, poisson.pmf(x, 15), 'bo', ms=8, label='poisson pmf')
plt.savefig('fig1.4.png')
plt.show()
