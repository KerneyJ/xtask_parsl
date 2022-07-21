#!/bin/sh

source ../dev/bin/activate

# test noop
for ops in 500 1000 1500 2000 2500 3000 3500 4000 4500 5000 5500 6000 6500 7000 7500 8000 8500 9000 9500 10000
do
    python3 func.py htex_test noop $ops -d benchmarks/laptop_benchmark
done

# test fib
for n in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
do
    python3 func.py htex_test fib $n -d benchmarks/laptop_benchmark
done
