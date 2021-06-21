#!/bin/sh

#$ -N VEP  #name
#$ -cwd  #current dir
#$ -V
#$ -l h_rt=24:00:00   #runtime
#$ -l h_vmem=8G


# Module load
module load igmm/apps/vep/97

echo python gwas_library_vep_loop_v2.py $SGE_TASK_ID

python gwas_library_vep_loop_v2.py $SGE_TASK_ID
