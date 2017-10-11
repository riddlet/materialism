#!/bin/bash
#group_submit.sh

# Directives
#PBS -N materialism_w2v
#PBS -W group_list=yetipsych
#PBS -l nodes=1:ppn=2
#PBS -l mem=4096mb
#PBS -l walltime=24:00:00
#PBS -M tar2119@columbia.edu
#PBS -m a
#PBS -V

# Set output and error directories
#PBS -o localhost:/vega/psych/users/tar2119/materialism/out
#PBS -e localhost:/vega/psych/users/tar2119/materialism/err
echo '1 node, 2 processors, 4096mb, walltime 24hrs'
date
$1

module load anaconda/2.7.8
python $1
date


#to run multiple files: for i in *.py; do qsub -F "$i$" group_submit.sh; done
# End of script