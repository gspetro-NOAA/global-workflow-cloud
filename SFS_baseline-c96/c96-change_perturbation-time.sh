#!/bin/bash

 set -x

 DTG=1994050100

 ymd=${DTG:0:8}
 hour=${DTG:8:2}

 RUN=gefs
 source=/work2/noaa/epic/weihuang/ICs/REPLAY_ICs/C96mx100/C96C96mx100/20240610/${RUN}.${ymd}/${hour}
 target=/work2/noaa/epic/weihuang/ICs/REPLAY_ICs/C96mx100/C96C96mx100/20240610/${RUN}.${ymd}/${hour}

 PRE_DTG=$( date -u -d"${DTG:0:4}-${DTG:4:2}-${DTG:6:2} ${DTG:8:2}:00:00 6 hours ago" +%Y%m%d%H )

 members=$( ls -d ${source}/*/ )

 for member in ${members}; do
    member=$( basename ${member} )

    srcdir=${source}/${member}/analysis/atmos
    oldflnm=${srcdir}/${ymd}.000000.fv3_perturbation.nc

    tardir=${target}/${member}/analysis/atmos
    newflnm=${tardir}/${ymd}.030000.fv3_perturbation.nc
   #cp ${oldflnm} ${newflnm}

    srcdir=${source}/${member}/analysis/ocean
    oldflnm=${srcdir}/${ymd}.000000.mom6_perturbation.nc

    tardir=${target}/${member}/analysis/ocean
    newflnm=${tardir}/${ymd}.030000.mom6_perturbation.nc
    cp ${oldflnm} ${newflnm}
 done

