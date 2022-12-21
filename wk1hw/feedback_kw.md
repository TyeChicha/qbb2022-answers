# Week 1 Genome Assembly -- Feedback

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 0.75 + 1 = 9.75 points out of 10 possible points

1. Question 1.1, 1.4 how many reads (0.5 pts each)

  * Yes, how did you get these numbers? --> +1

2. Question 1.2, 1.4 simulation script(s)

  * script is set up only for question 1.4, should be more generalizable, taking in command line arguments or calling functions with parameters that can be changed

3. Question 1.2, 1.4 plotting script(s)

  * script is set up only for question 1.4, should be more generalizable, taking in command line arguments or calling functions with parameters that can be changed

4. Question 1.2, 1.4 histograms with overlaid Poisson distributions (0.5 pts each)

  * Consider adding plot titles in order to distinguish the 5x from the 15x coverage


5. Question 1.3, 1.4 how much of genome not sequenced/comparison to Poisson expectations (0.5 pts each, 0.25 for answer and 0.25 for code)

  * --> +1
  * are these differences a problem or close enough?

6. Question 2 De novo assembly (0.5 pts each, 0.25 for answer and 0.25 for code)

  * number of contigs --> +0.5
  * total length of contigs --> +0.5

7. Question 2 De novo assembly cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * size of largest contig --> +0.5
  * contig n50 size --> +0.5

8. whole genome alignment (0.33 pts each, 0.33/2 for answer and 0.33/2 for code)

  * average identity --> +0.33
  * length of longest alignment --> +0.33
  * how many insertions and deletions in assembly --> +0.33, you are correct, but note that insertions in the reference are technically deletions in the assembly.

9. decoding the insertion (0.5 pts each, 0.25 for answer and 0.25 for code)

  * position of insertion in assembly --> +0.5
  * length of novel insertion --> +0.25 your length is off. You want end - start + 1, so 714. 27500 - 26787 + 1. The plus one is because you need to make sure to count the last number. When you're counting from 1 to 10, you count 10 numbers. But 10-1 is only 9.

10. decoding the insertion cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * DNA sequence of encoded message --> +0.5
  * secret message --> +0.5
