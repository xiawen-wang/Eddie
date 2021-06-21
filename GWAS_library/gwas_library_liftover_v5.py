from subprocess import call
import subprocess
import datetime
import time
import glob
import sys
import os

job_id = sys.argv[1]

species = ['hg19', 'C57B6J', 'Rattus', 'micOch1', 'jacJac1', 'oryCun2', 'panTro4', 'gorGor3', 'ponAbe2', 'rheMac3', 'oviBos', 'oviAri3', 'bosTau8', 'canFam3', 'felCat8', 'loxAfr3']
species_names = ['human', 'mouse', 'rat', 'prairie_vole', 'egyptian_jerboa', 'rabbit', 'chimpanzee', 'gorilla', 'orangutan', 'macaque', 'musk_ox', 'sheep', 'cow', 'dog', 'cat', 'elephant']

## liftOver for each file
input_files = glob.glob('GWAS_library/liftOver_input/temp_v2/*.bed')
input_files.sort()
output_dir = 'GWAS_library/liftOver_output/split_output_v4/'
lift_genome = 'hg19'
for i in range(len(species)):
    #for j in range(len(input_files)):
        print(species[i])
        print(str(datetime.datetime.now()))
        halLiftover = '/exports/cmvm/eddie/sbms/groups/young-lab/rob/scripts/hal/halLiftover /exports/cmvm/eddie/sbms/groups/young-lab/rob/genomes/1509_outgroups.hal ' + lift_genome + ' ' + input_files[int(job_id)-1] + ' ' + species[i] + ' ' + output_dir + lift_genome + '_' + species[i] + '_' + str(job_id) + '.bed'
        print(halLiftover,'\n\n')
        call(halLiftover, shell=True)
        call('gzip ' + output_dir + lift_genome + '_' + species[i] + '_' + str(job_id) + '.bed', shell=True)
