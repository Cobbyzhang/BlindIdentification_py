# !/usr/bin/env python
# coding:UTF-8
#
# Created on 2017/4/19
# Author: CobbyZhang
#
#

import scipy.io as scio

from ErrorAnalysis.ErrorSet import ErrorSet

dataFile = './Data/G2_Enumerate.mat'
data = scio.loadmat(dataFile)
ErrorSetCell = data['ErrorSetCell'][0]
v = data['v']
t = data['t']
# print ErrorSetCell
a = ErrorSet(ErrorSetCell, v, t)
# a.show_error(2, 0)
print a.error_number, '\n', a.totality, '\n', t
# print [(int(errors[:-2:2]), int(errors[1:-2:2])) for errors in ErrorSetCell[2]]
# print [(errors[::2], errors[1::2]) for errors in ErrorSetCell[2]
#        if int(errors[:-2:2]) == 0 or int(errors[:-2:2]) == 0]
# print ErrorSetCell[3]
# print max(data['v'])
# print data['t']

