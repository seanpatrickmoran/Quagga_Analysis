
# StripeCaller - Quagga Analysis and workflow

### Summary
This is the workflow explanation and support for how to optimize and process downstream of Quagga (https://github.com/dmcbffeng/StripeCaller/)

Once we decided on a 3C family file, we visualize the file using lighthouse or juicebox to determine a diagnostic stripe to check that Quagga picks up on the clear stripe. Then, run quagga on a series of parameters on a single chromosome, like in parameter_screen.sh.

Now that we have stripe files, we first examine the outputs against our diagnostic region to choose the ideal parameters (notebook 1); pick the file that best matches the diagnostic region. Also, Using "write_stripe_histrograms.py", we may check if the length of stripes is in a reasonable range. Then, re-run Quagga for all chromosomes on the hic/mcool file with the optimal parameters.

Second, aggregrate stripe integrity is checked with standard APA analysis (notebook 2).

Third, once satisfied, we do intersecting or non intersecting intervals to assign CTCF or enhancer-promoter activity (notebook 3).

Finally, we perform epigenomic pileups with the assistance of "process_for_epi.py" to load our factors into .npy and form the correct filestructure (notebook 4).
