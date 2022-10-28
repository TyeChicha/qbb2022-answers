#!/usr/bin/env python

import sys

import numpy 
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math 

def main():
    # in1_fname should be ddCTCF
    # in2_fname should be dCTCF
    # bin_fname should be bed file with bin locations
    
    in1_fname, in2_fname, bin_fname, out_fname = sys.argv[1:5]
    data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    chrom = b'chr15'
    start = 11170245
    end = 12070245
    start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1
                                       
    
    #dCTCF
    mat1=numpy.zeros((end_bin-start_bin,end_bin-start_bin))
    for i in range(end_bin-start_bin):
        for j in range(end_bin-start_bin):
            temp=data1[(data1['F1']==i+start_bin) & (data1['F2']==j+start_bin)]
            if not temp.size>0:
                continue
            mat1[i][j]=temp[0][2]
    #ddCTCF
    mat2=numpy.zeros((end_bin-start_bin,end_bin-start_bin))
    for i in range(end_bin-start_bin):
        for j in range(end_bin-start_bin):
            temp=data2[(data2['F1']==i+start_bin) & (data2['F2']==j+start_bin)]
            if not temp.size>0:
                continue
            mat2[i][j]=temp[0][2]
    #diff
    mat3=mat2-mat1
    #mat3=numpy.log(mat3)
    mat3=remove_dd_bg(mat3)
    
    #mat1=numpy.nan_to_num(mat3,nan=0,neginf=0)
    #mat2=numpy.nan_to_num(mat3,nan=0,neginf=0)
    numpy.nan_to_num(mat3,copy=False,nan=0,neginf=0)
    print(mat3)
    
    
    fig,ax=plt.subplots(ncols=3)
    ax[0].imshow(mat1,vmin=0,vmax=300,cmap='magma')
    ax[1].imshow(mat2,vmin=0,vmax=300,cmap='magma')
    ax[2].imshow(mat3,norm=colors.CenteredNorm(),cmap='seismic')
    plt.savefig(out_fname)
    plt.show()
    
def remove_dd_bg(mat):
    N = mat.shape[0]
    mat2 = numpy.copy(mat)
    for i in range(N):
        bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
        mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
        if i > 0:
            mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
    return mat2

if __name__ == "__main__":
    main()