#!/bin/bash

for b in 1 2 4 8 16
do
	for d in 0 10 1000 10000
	do
		for _ in {1..10}
		do
			python3 func.py htex $b 8 noop 10000 -s $d >> cdfkdirex_$((b * 8))_$((d)).txt
		done
	done
done

for w in 1 2 4
do
	for d in 0 10 1000 10000
	do
		for _ in {1..10}
		do
			python3 func.py htex 1 $w noop 10000 -s $d >> cdfkdirex_$((w))_$((d)).txt
		done
	done
done
