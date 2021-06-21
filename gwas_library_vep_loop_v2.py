from subprocess import call
import subprocess
import datetime
import time
import glob
import sys

job_id = int(sys.argv[1])

vep_input=glob.glob('GWAS_library_vep/vep_input/vep_temp_*.txt')
vep_input.sort()

output_dir='GWAS_library_vep/vep_output/'
#for i in range(len(vep_input)):
print(str(datetime.datetime.now()),'\n\n')
print(vep_input[job_id-1])
file_name=vep_input[job_id-1].split('/')[2].split('_')[2]
vep = 'vep --database -i ' + vep_input[job_id-1] + ' -o ' + output_dir + 'vep_ouput_' + file_name +' --port 3337'
print(vep)
silent_call=call(vep, shell=True)
