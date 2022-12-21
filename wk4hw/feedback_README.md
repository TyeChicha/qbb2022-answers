This is a really awesome start. You're almost there. All your plink commands look good, and your PCA plot and AF plot are both correct. I will day it is good practice to make sure you label your plots (i.e. the AF plot) so we know what we're looking at.

You're close to having the manhattan plot, but there's a few issues. Your scatter plot can't just have the `SNP` column on the x-axis, because then matplotlib will just try to plot all the rsids which 1) doesn't make sense and 2) is a whole bunch of strings (which is why there's just a solid black bar where the x-axis labels are). Your x-axis should either be the position of each variant in the genome, or at least their relative position (i.e. the first variant would be 1, the second would be 2, etc) (-3 points)

Also make sure that in your manhattan plot, you're not also plotting the pvals of the covariates, (there's a `TEST` column in the plink output that might be able to help you)

We still need the box plot and your answer for question 5 (-2.5 points)

(4.5/10)

REGRADE 12/21/22 -- Dylan

Good work on this, however there are some things that still need work.

1. When you run your PCA, you're actually finding the top 20 PCs, rather than the top 10, because you didn't specify in your command. This will affect your regression, because you're including more covariates. (no points deducted)
2. There are a few wonky things going on with your manhattan plot. First, when you run the regression, the way you have your command set up, you're actually running two different types of regression. The `--assoc` flag does something called a Wald test, when we want to just do simple linear regression. That said, you also included the `--linear` flag, which DOES do what we want. The only problem is that you're using the Wald test results in your code. Funnily enough, this actually circumvents one other issue you might have with the linear regression results. The linear regression results actually also have results for the covariates, so if you do use the linear regression results, you'll need to remove the covariate results before plotting. (-0.5 point)
2. The FINAL issue is that while you are plotting the position of each variant on the x-axis, you don't take the chromosome into account, and so you're overlaying all the chromosomes on top of each other. This can be addressed easily by just plotting the index of each variant, rather than the position itself. (-0.25 point)
3. When you found your top SNP, my guess is that you used the bash `sort` tool, which is a totally okay way to do it, but you need to include the `-g` or `-n` flags so that it sorts the column numerically, because otherwise, any number that's formatted like `1.24e-10` will look BIGGER than anything that starts with zero, like `0.143`. So you're finding a pretty significant SNP, but not the MOST significant. The boxplot itself however looks great. (-0.25 point)
3. We're missing your answer for part 7 (-1 point)

Everything else looks great!

(8/10)
