#!/usr/bin/python
# -*- coding:UTF-8 -*-
#filename: using_sys.py


import sys
from swap import swap
from using_name import run

print('命领行:')
for i in sys.argv:
    print i

print('the path', sys.path, '\\n')

print "the python version: ", sys.copyright

print swap(12,33)

run()
