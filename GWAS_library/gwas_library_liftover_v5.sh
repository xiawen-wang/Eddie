#!/bin/sh

#$ -N gwas_library_liftover #name
#$ -cwd  #current dir
#$ -l h_rt=24:00:00   #runtime
#$ -l h_vmem=4G


module unload python

# Module load
module load igmm/apps/python/3.7.3 igmm/apps/R/3.3.0 igmm/apps/BEDTools/2.25.0 igmm/libs/ncurses/6.0 igmm/apps/samtools/1.3 igmm/apps/bcftools/1.3 igmm/apps/vcftools/0.1.13 igmm/libs/ensembl_api/86 igmm/apps/last/847 igmm/compilers/gcc/5.5.0

module list
 
echo python gwas_library_liftover_v5.py $SGE_TASK_ID

python gwas_library_liftover_v5.py $SGE_TASK_ID
