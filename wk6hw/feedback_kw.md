## Week 6 -- 10 points possible

1 + 1 + 1 + 0.33 + 0 + 0.5 + 0.66 + 1 + 1 + 1 = 7.5 of 10 points possible

1. Given data question: What percentage of reads are valid interactions?

2. Given data question: What constitutes the majority of invalid 3C pairs?/What does it mean?

3. Script set up to (0.5 pts each)

  * read in data  
  * Filter data based on location  

4. Script set up to log transform the scores

* only took the log for the difference matrix?

5. Script set up to shift the data by subtracting minimum score value

* I don't see this

6. Script set up to convert sparse data into square matrix

* I think you convert it to a square matrix, but don't fill the whole matrix, only half of it

7. Script set up to (0.33 pts each)

  * remove distance dependent signal
  * smooth --> Don't see this
  * subtract --> subtract after the previous steps, not before

8. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for subset dataset (0.33 pts each ddCTCF/dCTCF/difference)

9. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for full dataset (0.33 pts each ddCTCF/dCTCF/difference)

10. Heatmap questions (0.33 pts each)

  * See the highlighted difference from the original figure?
  * impact of sequencing depth?
  * highlighted signal indicates?

Possible Bonus points:

1. Insulation script set up to (0.25 pts each)

  * read in data
  * filter data based on location
  * log transform the data
  * shift the data by subtracting minimum value

2. Insulation script set up to (0.5 pts each)

  * convert sparse data into square matrix
  * find the insulation score by taking mean of 5x5 squares of interactions around target

3. Turned in the plot of the heatmap + insulation scores below (0.5 pts each panel)
