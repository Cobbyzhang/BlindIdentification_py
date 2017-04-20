#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time    : 17-4-20 下午8:33
# @Author  : Cobby Zhang
# @Site    : 
# @File    : fromattransferutils.py
# @Software: PyCharm Community Edition


import numpy as np
import math
import sys

try:
    import scipy.linalg
except ImportError:
    print "Error: Program requires scipy (see: www.scipy.org)."
    sys.exit(1)


######################################################################
# Decimal to any base conversion.
# Convert 'num' to a list of 'l' numbers representing 'num'
# to base 'base' (most significant symbol first).
######################################################################
def dec2base(num, base, l):
    s = range(l)
    n = num
    for i in range(l):
        s[l-i-1] = n % base
        n = int(n/base)
    if n != 0:
        print 'Number ', num, ' requires more than ', l, 'digits.'
    return s


######################################################################
# Conversion from any base to decimal.
# Convert a list 's' of symbols to a decimal number
# (most significant symbol first)
######################################################################
def base2dec(s, base):
    num = 0
    for i in range(len(s)):
        num = num * base + s[i]
    return num


######################################################################
#
#
#
######################################################################
