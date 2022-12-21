Great work! Just a couple minor comments:

1. When you're doing your dendrogram, it looks like you're trying to make the dendrogram for transcripts, but limiting it to only plot the top 10 levels of this dendrogram. Which isn't quite what we're looking for. Instead we wanted to plot the entire SAMPLE dendrogram. To do this, you'll actually want to run `linkage` on the *transpose* of the expression matrix, and then run `dendrogram` on that. (-0.25 point)
2. It looks like you used 0.3 as your alpha for FDR correction (i.e. 30%), which is a bit of an... unconventional threshold, and means that more of your results are significant. We did ask you to use a 0.1 (10%) FDR threshold, but this is not a big deal at all (no points deducted)

Everything else looks really good though. Excellent work!

(9.75/10)
