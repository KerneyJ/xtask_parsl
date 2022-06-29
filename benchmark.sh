#!/bin/sh

#source ../dev/bin/activate
#
## test noop
#for ops in 500 1000 1500 2000 2500 3000 3500 4000 4500 5000 5500 6000 6500 7000 7500 8000 8500 9000 9500 10000
#do
#    python3 func.py "htex1" "noop" $ops "-d benchmarks/bench-prof"
#done
#
# test fib
#for n in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#do
#    python3 func.py "htex1" "fib" $n "-d benchmarks/bench-prof"
#done

python3 func.py htex1 noop 500 -d benchmarks/parsl_test
