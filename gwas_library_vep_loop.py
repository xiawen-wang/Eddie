from subprocess import call
import subprocess
import datetime
import time
import glob

vep_input=glob.glob('GWAS_library_vep/vep_input/vep_temp_*.txt')
vep_input.sort()

output_dir='GWAS_library_vep/vep_output/'
for i in range(len(vep_input)):
    print(str(datetime.datetime.now()),'\n\n')
    print(vep_input[i])
    file_name=vep_input[i].split('/')[2].split('_')[2]
    vep = 'vep --database -i ' + vep_input[i] + ' -o ' + output_dir + 'vep_ouput_' + file_name +' --port 3337'
    print(vep)
    silent_call=call(vep, shell=True)
