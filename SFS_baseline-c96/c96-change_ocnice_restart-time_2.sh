#!/bin/bash

 set -x

 DTG=1994050100
 ymd=${DTG:0:8}
 hour=${DTG:8:2}

 PRE_DTG=$( date -u -d"${DTG:0:4}-${DTG:4:2}-${DTG:6:2} ${DTG:8:2}:00:00 6 hours ago" +%Y%m%d%H )
 pre_ymd=${PRE_DTG:0:8}
 pre_hour=${PRE_DTG:8:2}

 RUN=gefs
 source=/work2/noaa/epic/weihuang/ICs/REPLAY_ICs/C96mx100/C96C96mx100/20240610/${RUN}.${pre_ymd}/${pre_hour}
 target=/work2/noaa/da/weihuang/run/COMROOT/c96sfs/${RUN}.${pre_ymd}/${pre_hour}

 members=$( ls -d ${source}/*/ )

 for member in ${members}; do
    member=$( basename ${member} )

    srcdir=${source}/${member}/model/ocean/restart
    oldflnm=${srcdir}/${ymd}.030000.MOM.res.nc

    tardir=${target}/${member}/model/ocean/restart
    newflnm=${tardir}/${ymd}.000000.MOM.res.nc
    cp ${oldflnm} ${newflnm}

    srcdir=${source}/${member}/model/ice/restart
    oldflnm=${srcdir}/${ymd}.030000.cice_model.res.nc

    tardir=${target}/${member}/model/ice/restart
    newflnm=${tardir}/${ymd}.000000.cice_model.res.nc
    cp ${oldflnm} ${newflnm}
 done

