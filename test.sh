#!/bin/bash

source ../forkenv/bin/activate && pip freeze | xargs pip uninstall -y
../forkenv/bin/python3 -m pip install ../parsl/.
python3 func.py htex_lq fib 15 -d benchmarks/parsl_test
