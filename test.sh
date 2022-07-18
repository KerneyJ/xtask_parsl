#!/bin/sh

source ../forkenv/bin/activate && pip freeze | xargs pip uninstall -y
../forkenv/bin/python3 -m pip install ../parsl/.
python3 func.py htex_test noop 10 -d benchmarks/parsl_test
