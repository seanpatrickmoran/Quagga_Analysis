#!/bin/bash
  
SPRITE="/nfs/turbo/umms-drjieliu/proj/4dn/data/SPRITE/mESC/4DNFIQHH2MMH.mcool"

stripe_caller --hic $SPRITE --output 10000nt_MR15000000_ML50000_MD2000000_MW20000_WS2_SG1RH0.3_NSTR5_WholeGenome_mm10_4DNFIQHH2MMH.txt --chr chr1 chr2 chr3 chr4 chr5 chr6 chr7 chr8 chr9 chr10 chr11 chr12 chr13 chr14 chr15 chr16 chr17 chr18 chr19 chrX chrY --rg 'mm10' --max_range 15000000 --resolution 10000 --min_length 50000 --min_distance 2000000 --window_size 2 --sigma 1 --rel_height 0.3 --norm balanced --thr 0.15 --nstrata_blank 5 --max_width 20000

# wc -l 10000nt_MR15000000_ML50000_MD2000000_MW20000_WS2_SG1RH0.3_NSTR5_WholeGenome_mm10_4DNFIQHH2MMH.txt
