#!/bin/bash

source ../exp/bin/activate

# Experiment 1
for ops in 2048 4096 8192 16384 32768  65536 131072 262144 524288 1048576
do
    python3 func.py htex_exp1 noop $ops -d benchmarks/experiment1
done

for n in 5 10 15 20 25 30
do
    python3 func.py htex_exp1 fib $n -d benchmarks/experiment1
done

# Experiment 2
for ops in 2048 4096 8192 16384 32768  65536 131072 262144 524288 1048576
do
    python3 func.py htex_exp2 noop $ops -d benchmarks/experiment2
done

for n in 5 10 15 20 25 30
do
    python3 func.py htex_exp2 fib $n -d benchmarks/experiment2
done

# Experiment 3
for ops in 2048 4096 8192 16384 32768  65536 131072 262144 524288 1048576
do
    python3 func.py htex_exp3 noop $ops -d benchmarks/experiment3
done

for n in 5 10 15 20 25 30
do
    python3 func.py htex_exp3 fib $n -d benchmarks/experiment3
done

# Experiment 4
for ops in 2048 4096 8192 16384 32768  65536 131072 262144 524288 1048576
do
    python3 func.py htex_exp4 noop $ops -d benchmarks/experiment4
done

for n in 5 10 15 20 25 30
do
    python3 func.py htex_exp4 fib $n -d benchmarks/experiment4
done

# Experiment 5
for ops in 2048 4096 8192 16384 32768  65536 131072 262144 524288 1048576
do
    python3 func.py htex_exp5 noop $ops -d benchmarks/experiment5
done

for n in 5 10 15 20 25 30
do
    python3 func.py htex_exp5 fib $n -d benchmarks/experiment5
done

# Experiment 6
for ops in 2048 4096 8192 16384 32768  65536 131072 262144 524288 1048576
do
    python3 func.py htex_exp6 noop $ops -d benchmarks/experiment6
done

for n in 5 10 15 20 25 30
do
    python3 func.py htex_exp6 fib $n -d benchmarks/experiment6
done

# Experiment 7
for ops in 2048 4096 8192 16384 32768  65536 131072 262144 524288 1048576
do
    python3 func.py htex_exp7 noop $ops -d benchmarks/experiment7
done

for n in 5 10 15 20 25 30
do
    python3 func.py htex_exp7 fib $n -d benchmarks/experiment7
done

# Experiment 8
for ops in 2048 4096 8192 16384 32768  65536 131072 262144 524288 1048576
do
    python3 func.py htex_exp8 noop $ops -d benchmarks/experiment8
done

for n in 5 10 15 20 25 30
do
    python3 func.py htex_exp8 fib $n -d benchmarks/experiment8
done
