#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 0006 11:03
# @Author  : Arliki
# @Contact : hdknxycz@outlook.com 
# @Site    : 
# @File    : myfunction.py
# @Software: PyCharm
import re
class ComRe(object):
    '''判断输入的类型'''
    def input_type(a):
        atype=re.search('[a-zA-Z]+?',a)
        if atype:
            return str
        else:
            atype=re.search('^(\-|\+)?\d+\.\d+$',a)
            if atype:
                return float
            else:
                atype=re.search('\W+',a)
                if atype:
                    return str
                else:
                    return int