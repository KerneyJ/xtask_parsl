#!/bin/bash
source ../xq/bin/activate

for n in $(seq -f "%02g" 5 5 30)
do
	for w in 1 2 4 8 16 32 64 128
	do
		for _ in {1..10}
		do
			python3 func.py xq 1 $w fib $n -d benchmarks/xqueue >> xqfib${n}-$w.txt
		done
	done
done
