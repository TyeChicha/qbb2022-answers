This is a really awesome start. You're almost there. All your plink commands look good, and your PCA plot and AF plot are both correct. I will day it is good practice to make sure you label your plots (i.e. the AF plot) so we know what we're looking at.

You're close to having the manhattan plot, but there's a few issues. Your scatter plot can't just have the `SNP` column on the x-axis, because then matplotlib will just try to plot all the rsids which 1) doesn't make sense and 2) is a whole bunch of strings (which is why there's just a solid black bar where the x-axis labels are). Your x-axis should either be the position of each variant in the genome, or at least their relative position (i.e. the first variant would be 1, the second would be 2, etc) (-3 points)

Also make sure that in your manhattan plot, you're not also plotting the pvals of the covariates, (there's a `TEST` column in the plink output that might be able to help you)

We still need the box plot and your answer for question 5 (-2.5 points)

(4.5/10)
