#!/bin/bash

source ../testenv/bin/activate
pip3 freeze | xargs pip uninstall -y
pip3 install ../parsl/.
pip3 install six
python3 func.py htex 1 4 fib 5 -d benchmarks/parsl_test
