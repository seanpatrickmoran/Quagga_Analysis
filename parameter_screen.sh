#!/bin/bash

for MR in 10000000 15000000
do
    for ML in 50000
    do
        for MD in 2000000 #500000
        do
            for M_W in 50000
            do
                for WS in 7
                do
                    for SG in 1
                    do
                        for RH in $(seq 0.1 0.2 0.3)
                        do
                            for NSTR in 0 5 10
                            do
                                for RES in 5000
                                do
                                    for CHR in 7
                                    do
                                        stripe_caller --hic /nfs/turbo/umms-drjieliu/proj/4dn/data/bulkHiC/GM12878/GM12878.hic --output ${RES}nt_MR${MR}_ML${ML}_MD${MD}_MW${M_W}_WS${WS}_SG${SG}RH${RH}_NSTR${NSTR}_CHR${CHR}_hg38GM12878.txt --chr chr${CHR} --rg 'hg38' --max_range ${MR} --resolution $RES --min_length ${ML} --min_distance ${MD} --window_size ${WS} --sigma ${SG} --rel_height ${RH} --norm balanced --thr 0.15 --nstrata_blank ${NSTR} --max_width ${M_W}
                                        
                                        wc -l ${RES}nt_MR${MR}_ML${ML}_MD${MD}_MW${M_W}_WS${WS}_SG${SG}RH${RH}_NSTR${NSTR}_CHR${CHR}_hg38GM12878.txt
                                    done
                                done
                            done
                        done
                    done
                done
            done
        done
    done
done
