#!/bin/bash

cd /scratch/jb6504/goldmine/goldmine/scripts/hpc/lotkavolterra

sbatch --array=0-4 test_lv_maf.sh
sbatch --array=0-4 test_lv_scandal.sh
sbatch --array=0-4 test_lv_rascandal.sh
sbatch --array=0-4 test_lv_scandal_cv.sh
