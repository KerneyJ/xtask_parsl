#!/bin/bash
source ../dev/bin/activate
for n in 5 10 15 20
do
	for i in {1..100}
	do
		python3 func.py htex_exp1w fib $n -d benchmarks/lq >> mqueue_fib$n.txt
	done
done
