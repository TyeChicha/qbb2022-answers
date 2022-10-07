Great start! The algorithm itself is almost entirely correct. There are just a few minor issues with the algorithm, and then you also need to set up the input and output:

When you're intializing the traceback matrix, the first row should all be `h` and the first column should all be `v`, so that traceback can handle leading gaps (this will be relevant for the DNA alignment) (-0.25)

When you're doing traceback, you're only ever adding character from `sequence1`. You should be adding character from `sequence1` to the sequence1 alignment, and characters from `sequence2` to the `sequence2` alignment. It also looks like you might have `h` and `v` backwards. `h` should be a gap in sequence 1, and `v` should be a gap in sequence 2 (-0.5).

Other than these minor algorithmic issues, you need to read in the FASTA, scoring matrix, and gap penalty using `sys.argv`, as well as a filename to write the alignment to (-2.5)

You also need to actually write the alignments to the specified output file, as well as output the alignment stats we asked for (# gaps, and alignment score) (-2)

4.75/10
