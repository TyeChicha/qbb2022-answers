#!/usr/bin/env python

import numpy as np
import sys


#========================#
# Set sequences to align #
#========================#

# In the homework assignment, you'll reading sequences from a
# FASTA file. For the live-coding, we'll define them
# explicitly in the script.

sequence1 = 'TGTTACGG'
sequence2 = 'GGTTGACTA'


#===========================================================#
# Read in match, mismatch, and gap scores from command line #
#===========================================================#

# We can use `sys.argv` to read arguments in from the command
# line, stored in a list. The first thing in the list is
# always the name of the script.



# The rest of the elements of the list are any arguments = sys.argv[1:]
# passed when we run the script in the command line



# Assuming three arguments: match score, mismatch score, and
# gap penalty, store these arguments as variables we can use
# in our script.
matchscore=float(sys.argv[1])
misscore=float(sys.argv[2])
gappen=float(sys.argv[3])

#============================#
# Playing around with arrays #
#============================#

# Numpy is a Python package built around matrices (arrays).
# You can think of an array as a (potentially)
# multi-dimensional list. In fact, a 2D numpy array is
# essentially a list of lists. We can create a numpy
# array using the `np.array()` function.
#listoflist=[[1,2,3],[4,5,6],[7,8,9]]
#myarray=np.array(listoflist)

# If we want to know what the dimensions of our array
# are, we can check the `.shape` attribute

#dimensions=myarray.shape

# Just like we can index lists, we can also index numpy
# arrays. When we index a numpy array, we first index
# the rows, then the columns.



# Like with lists, numpy arrays also support item assignment.



# We can also loop through numpy arrays. When we loop through
# a 2D array, we loop through the rows



# Because each row is just a 1D numpy array, we can also loop
# through the row itself



# We can also use the range() function to loop through each
# value in the array




#=====================#
# Initialize F-matrix #
#=====================#

# The first thing we need to do is create an empty F-matrix.
# The number of rows should be equal to the length of
# sequence1 plus one (to allow for leading gaps). Similarly,
# the number of columns should be equal to the length of
# sequence2 plus one.

fmatrix=np.zeros((len(sequence1)+1, len(sequence2)+1))
tmatrix=np.empty((len(sequence1)+1, len(sequence2)+1),dtype=str)

#tmatrix=np.empty_like(fmatrix, dtype=None)


# Now we need to fill in the values in the first row and
# first column, based on the gap penalty. Let's fill in the
# first column.

for j in range(fmatrix.shape[1]):
    fmatrix[0][j]=j*gappen
    tmatrix[0][j]='z'
# Now fill in the first row

for i in range(fmatrix.shape[0]):
    fmatrix[i][0]=i*gappen
    tmatrix[i][0]='z'

#=======================#
# Populate the F-matrix #
#=======================#

# Now that we've filled in the first row and column, we need
# to go row-by-row, and within each row go column-by-column,
# calculating the scores for the three possible alignments
# and storing the maximum score

for i in range(1,fmatrix.shape[0]):
    for j in range(1,fmatrix.shape[1]):
        if sequence1[i-1]==sequence2[j-1]:
            d=fmatrix[i-1][j-1]+matchscore
        else:
            d=fmatrix[i-1][j-1]+misscore
        h=fmatrix[i][j-1]+ gappen
        v=fmatrix[i-1][j]+ gappen
        fmatrix[i][j]=max(d,v,h)
        if (max(d,v,h)==d):
            tmatrix[i][j]='d'
        elif (max(d,v,h)==h):
            tmatrix[i][j]='h'
        elif (max(d,v,h)==v):
            tmatrix[i][j]='v'
        else:
            print("Error: max did not match up with valid values (d, v, or h).")
print(fmatrix)
print(tmatrix)
r=len(sequence1)
c=len(sequence2)
seq1=[]
seq2=[]
check=tmatrix
while tmatrix[r][c]!='z':
    if tmatrix[r][c] == 'd':
        seq1.append(sequence1[r-2])
        seq2.append(sequence1[c-2])
        check[r][c]='x'
        r-=1
        c-=1
    elif tmatrix[r][c] == 'h':
        seq1.append(sequence1[r-2])
        seq2.append('-')
        check[r][c]='x'
        c-=1
    elif tmatrix[r][c] == 'v':
        seq1.append('-')
        seq2.append(sequence1[c-2])
        check[r][c]='x'
        r-=1
print(check)
print(seq1[::-1])
print(seq2[::-1])
print(seq1)
print(seq2)
print(sequence1)
print(sequence2)

#====================#
# Print the F-matrix #
#====================#


#print(fmatrix)

#=========================#
# A primer on while loops #
#=========================#

# While loops are a useful tool in Python (and most other languages)
# that allows you to continue doing a process until some condition
# stops being met. If we want, we can have them mimic a for loop:

# Let's make a for loop that prints out the integers from 0 to 10
# (non-inclusive)


# We can do the exact same thing with a while loop


# While loops can also let us easily go backwards

