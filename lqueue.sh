#!/bin/bash

source ../forkenv/bin/activate
for i in {1..100}
do
	python3 func.py htex_exp1w fib 20 -d benchmarks/lq >> lqueue_fib20.txt
done

