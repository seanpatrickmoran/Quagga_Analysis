#!/bin/bash

CTCF="/nfs/turbo/umms-drjieliu/proj/Quagga/analysis/Revisions/HiChIP/4DNFI4XWVUT6.mcool"

stripe_caller --hic $CTCF --output 10000nt_MR10000000_ML50000_MD2000000_MW50000_WS7_SG1RH0.1_NSTR10_CHRALL_CTCF_hg38.txt --chr chr1 chr2 chr3 chr4 chr5 chr6 chr7 chr8 chr9 chr10 chr11 chr12 chr13 chr14 chr15 chr16 chr17 chr18 chr19 chr20 chr21 chr22 chrX chrY --rg 'hg38' --max_range 10000000 --resolution 10000 --min_length 50000 --min_distance 2000000 --window_size 7 --sigma 1 --rel_height 0.1 --norm NONE --thr 0.05 --nstrata_blank 10 --max_width 50000
