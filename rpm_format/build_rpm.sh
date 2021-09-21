#!/bin/sh

python3 setup.py bdist_rpm --requires='python3-configobj' --requires='python3 >= 3.6.8'
