#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time    : 17-4-19 下午7:14
# @Author  : Cobby Zhang
# @Site    : 
# @File    : ErrorSet.py
# @Software: PyCharm Community Edition

import numpy as np


class ErrorSet(object):
    __ErrorSetCell = []
    __v = []
    __k = 0
    __s = 0
    __degT = 0
    _error_number = []
    _totality = []
    _ber = []

    @property
    def error_number(self):
        return self._error_number

    @property
    def totality(self):
        return self._totality

    @property
    def ber(self):
        return self._ber

    def __init__(self,ErrorSetCell,v):
        self.__ErrorSetCell = ErrorSetCell
        self.__s = np.size(self.__ErrorSetCell)
        self.__k = np.size(v)
        self.__v = v
        self.__degT = np.max(v) - np.min(v)
        self._error_number = np.array([np.size(S) for S in self.__ErrorSetCell])
        self._totality = np.array([2 ** (2 * n) for n in range(1,self.__s + 1)])
        self._ber = 1.0 * self._error_number / self._totality

    def show_error(self, s, error_type=0):
        error_type = int(error_type)
        temp_set = []
        if error_type == 0:
            temp_set = [(errors[::2], errors[1::2]) for errors in self.__ErrorSetCell[s]]
        elif error_type == 1:
            temp_set = [(errors[::2], errors[1::2]) for errors in self.__ErrorSetCell[s]
                        if int(errors[:-2 * self.__degT:2]) == 0 or int(errors[:-2 * self.__degT:2]) == 0]
        elif error_type == 2:
            temp_set = [(errors[::2], errors[1::2]) for errors in self.__ErrorSetCell[s] if errors[::2] == errors[1::2]]
        elif error_type == 3:
            temp_set = [(errors[::2], errors[1::2]) for errors in self.__ErrorSetCell[s]
                        if int(errors[:-2 * self.__degT:2]) != 0 and int(errors[:-2 * self.__degT:2]) != 0
                        and errors[::2] != errors[1::2]]
        else:
            raise ValueError('无效的错误类型 %d'%error_type)
        print '错误类型%d共有%d种\n' % (error_type, len(temp_set)),temp_set

