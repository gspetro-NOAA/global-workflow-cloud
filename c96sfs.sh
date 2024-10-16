#!/bin/bash

 set -x

 source ~/.bashrc
 source workflow/gw_setup.sh

 HPC_ACCOUNT=epic \
        IDATE=1994050100 \
        pslot=c96sfs \
        RUNTESTS=/work2/noaa/gsienkf/weihuang/run \
        ./workflow/create_experiment.py \
        --yaml SFS_baseline-c96/SFS.yaml

