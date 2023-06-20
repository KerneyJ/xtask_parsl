#!/bin/bash
# task granulairty in microseconds
# first argument should signify type "cdfkdirex" or "pdfkhtex"

if [ $# -eq 0 ]
  then
    echo "Parsl type undefined options: cdfkdirex or pdfkhtex"
    exit
fi

for s in 0 1 10 100 1000 10000 
do
	for w in 1 2 4
	do
		for _ in {1..10}
		do
			python3 func.py htex 1 $w noop 10000 -s $s >> $1_$(($w))_$(($s))us.txt
		done
	done
	for b in 1 2 4 8 16
	do
		for _ in {1..10}
		do
			python3 func.py htex $b 8 noop 10000 -s $s >> $1_$((8 * $b))_$(($s))us.txt
		done
	done
done
