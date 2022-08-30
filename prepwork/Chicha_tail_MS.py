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

# This is SOOOO close! Your logic is sound and I really like how you used your
# first for loop to count the number of lines in the file. The only issue is in
# your if statement. You are trying to print the last "limit" lines, but you've
# got it hardcoded that you only print lines if length - count < 11. You need to
# rewrite the if statement to print if count >= length - limit. That way it 
# prints the length - limit, length - limit + 1, ..., length - 1 lines. Also
# make sure to comment your code. As you write longer scripts, it will help 
# other readers and you to keep track of what you were trying to do. You 
# clearly have a good grasp of what you're doing. Keep it up! - Mike