#!/bin/bash

source ../tagging/bin/activate
python3 func.py htex_test fib 10 -d benchmarks/tagging
python3 func.py htex_exp1 fib 10 -d benchmarks/tagging

python3 func.py htex_test fib 15 -d benchmarks/tagging
python3 func.py htex_exp1 fib 15 -d benchmarks/tagging
