#!/bin/bash

source ../cdfkenv/bin/activate
pip uninstall parsl -y
pip install ../parsl/.
