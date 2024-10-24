#!/bin/bash

 set -x

 source ~/.bashrc
 source workflow/gw_setup.sh

 HPC_ACCOUNT=${USER} \
	pslot=c96sfs \
	RUNTESTS=/lustre/$USER/run \
	./workflow/create_experiment.py \
        --yaml SFS_baseline-c96/SFS.yaml

