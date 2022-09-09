#!/usr/bin/env python

import sys
import numpy 
from scipy.stats import binomtest
from statsmodels.stats.multitest import multipletests
import seaborn as sns
import matplotlib.pyplot as plt

def simulate_coin_toss(n_tosses, prob_heads = 0.5, seed=None):
    '''
    Input: n_tosses, an integer, number of coin tosses to simulate
           prob_heads, a float, the probability the coin toss will return heads; default is 0.5, meaning a fair coin
           seed, an integer, the random seed that will be used in the simulation
    Output: results_arr, an array of 1's and 0's with 1's representing heads and 0's representing tails
    Resources: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    '''
    if seed is not None:
        numpy.random.seed(seed)
    results_arr = numpy.random.choice([0,1], size=n_tosses, p = [1-prob_heads, prob_heads])
    return (results_arr)

##print(numpy.sum(simulate_coin_toss(10)))


def perform_hypothesis_test(n_heads,n_tosses):
    binom_result=binomtest(n_heads,n_tosses)
    pval=binom_result.pvalue
    return pval
    
#print(perform_hypothesis_test(2,5))

def interpret_pvalue(pvals):
    interpreted=numpy.array(pvals) < 0.05
    return interpreted

#print(interpret_pvalue([0.03,0.05,0.07]))

def experiment(prob_heads, n_tosses, n_iters=100, seed=389, correctp=False):
    numpy.random.seed(seed)
    pval=[]
    for i in range(n_iters):
        results_arr=simulate_coin_toss(n_tosses,prob_heads=prob_heads)
        n_success=numpy.sum(results_arr)
        pval.append(perform_hypothesis_test(n_success, n_tosses))
    if correctp:
        pval=correct_pvals(pval)
    pvals_to_bools=interpret_pvalue(pval)
    power=compute_power(numpy.sum(pvals_to_bools),n_iters)
    return power

#print(experiment(0.2,30,n_iters=5))

def correct_pvals(pvals):
    corrected=multipletests(pvals,method="bonferroni")
    return corrected[1]
    
def compute_power(n_reject_correct, n_test):
    power= n_reject_correct/n_test
    return power
    
def heatmap(prob, toss, correct=False):
    heat=numpy.zeros([len(prob),len(toss)])
    for i, p in enumerate(prob):
        for j, t in enumerate(toss):
            heat[i, j]=experiment(p,t,correctp=correct)
    print(heat)
    fig, ax=plt.subplots()
    ax=sns.heatmap(heat,vmin=0.0, vmax=1.0, cmap="cividis",linewidths=.1, xticklabels=toss,yticklabels=prob)
    plt.xlabel('number of tosses')
    plt.ylabel('probability of heads')
    plt.title('Power of coin toss simulations')
    #plt.show()
    plt.savefig("power_heatmap.png")
probin=numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
tossin=numpy.array([10, 50, 100, 250, 500, 1000])
heatmap(probin,tossin)

# power2 = experiment(0.95, 10, correctp=True)
# print(power2)
#vmin, vmax, cmap, 


        