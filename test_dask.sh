#!/bin/bash
for w in 1 2 4 8 16 32 64 128
do
	for d  in 0 10 1000 10000
	do
		for _ in {1..10}
		do
			python3 dfunc.py $w $d >> dask_$(($w))_$(($d))us.txt
		done
	done
done
