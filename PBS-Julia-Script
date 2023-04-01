#!/bin/bash
 
#PBS -l walltime=03:00:00,select=1:ncpus=32:mem=16gb
#PBS -N RVM_Run
#PBS -m abe
#PBS -o MCMC-RVM_v2priorout.txt
#PBS -e MCMC-RVM_v2priorerr.txt
 
################################################################################

# In case you need to load modules
# module load  gcc/9.4.0  intel-mkl/2020.4.304 julia/1.6.1 

# To change to the working directory
# cd "/scratch/julia/GX"

JULIA_NUM_THREADS=32 julia "MCMC-Julia.jl"
