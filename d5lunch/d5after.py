#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats

fin=open(sys.argv[1])
data=np.genfromtxt(fin, dtype=None, encoding=None, names=True)

fig1,ax1=plt.subplots()

ax1.scatter(data['Mother_age'],data['mcount'],alpha=.6)
ax1.set_xlabel('Mom age')
ax1.set_ylabel('mutations passed')

plt.title('Mutations passed by Parents')

plt.xlim([15, 60])
plt.ylim([0, 100])   #ax.set_xlim is 
plt.savefig('ex2a.png')

fig2,ax2=plt.subplots()

ax2.scatter(data['Father_age'],data['fcount'],alpha=.6)
ax2.set_xlabel('Dad age')
ax2.set_ylabel('mutations passed')

plt.title('Mutations passed by Parents')

plt.xlim([15, 60])
plt.ylim([0, 100])
plt.savefig('ex2b.png')

# model = smf.ols(formula = "Mother_age ~ 1 + mcount", data = data)
# results = model.fit()
# results.summary()
#
# model = smf.ols(formula = "Father_age ~ 1 + fcount", data = data)
# results = model.fit()
# results.summary()

fathermodel = smf.ols(formula = "fcount ~ 1 + Father_age", data = data).fit()
#fresults = fathermodel.fit()
#print(fresults.summary())

mothermodel = smf.ols(formula = "mcount ~ 1 + Mother_age", data = data).fit()
#mresults = mothermodel.fit()
#print(mresults.summary())

fig3,ax3=plt.subplots()
ax3.hist(data['fcount'],alpha=.6,label='paternal count')
ax3.hist(data['mcount'],alpha=.6,label='maternal count')
ax2.set_xlabel('Dad age')
ax2.set_ylabel('mutations passed')
plt.legend()
#plt.xlim([15, 60])
#plt.ylim([0, 100])
plt.title('Parental vs Maternal mutation counts')
plt.savefig('ex2c.png')

print(stats.ttest_ind(data['mcount'],data['fcount']))

#predictions
new_data = data[0]
new_data.fill(0)
new_data['Father_age'] = 50.5
print(fathermodel.predict(new_data))


