'''
ex1
file = "random_snippet.vcf"
for line in open(file):
    print (line.strip("\n\r"))


ex2
file = "random_snippet.vcf"
for count,line in enumerate(open(file)):
    if(count==0):
        print(line.strip("\n\r"))

ex3
file = "random_snippet.vcf"
limit = 10
for count,line in enumerate(open(file)):
    if(count<limit):
        print(line.strip("\n\r"))
ex4
#
import sys
file = sys.argv[1]
limit = int(sys.argv[2])
for count,line in enumerate(open(file)):
    if(count<limit):
        print(line.strip("\n\r"))

ex5
import sys
file = sys.argv[1]
if(len(sys.argv)<3):
    limit=10
else
    limit = int(sys.argv[2])
for count,line in enumerate(open(file)):
    if(count<limit):
        print(line.strip("\n\r"))

ex6
import sys
file = sys.argv[1]
displayed=0
if(len(sys.argv)<3):
    limit=10
else
    limit = int(sys.argv[2])
for count,line in enumerate(open(file)):
    if(display<=limit and line[0]!="#"):
        print(line.strip("\n\r"))
        display=display+1

ex7
import sys
file = sys.argv[1]
displayed=0
length=0
if(len(sys.argv)<3):
    limit=10
else
    limit = int(sys.argv[2])
for length,line in enumerate(open(file)):
    pass
for count,line in enumerate(open(file)):
    if(display<=limit and line[0]!="#" and length-count<11):
        print(line.strip("\n\r"))
        display=display+1
'''

import sys
file = sys.argv[1]
display=0
length=0
if(len(sys.argv)>2):
    limit = int(sys.argv[2])
else:
    limit=10
for length,line in enumerate(open(file)):
    pass
for count,line in enumerate(open(file)):
    if(display<=limit and line[0]!="#" and length-count<11):
        print(line.strip("\n\r"))
        display=display+1
