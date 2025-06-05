#!/bin/bash

treated="./HCT-116-Rao2017/GSE104333_Rao-2017-treated_6hr_combined_30.hic"

stripe_caller --hic $treated --output 10000nt_MR15000000_ML50000_MD500000_MW50000_WS7_SG1RH0.1_NSTR0_WholeGenome_treated_hg19AUX.txt --chr chr1 chr2 chr3 chr4 chr5 chr6 chr7 chr8 chr9 chr10 chr11 chr12 chr13 chr14 chr15 chr16 chr17 chr18 chr19 chr20 chr21 chr22 chrX chrY --rg 'hg19' --max_range 15000000 --resolution 10000 --min_length 50000 --min_distance 500000 --window_size 7 --sigma 1 --rel_height 0.1 --norm balanced --thr 0.15 --nstrata_blank 0 --max_width 50000


