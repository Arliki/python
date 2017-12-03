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
    #判断输入的类型
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
    #组合成字典
    def to_dict(a,b,c=0):
        if isinstance(a,(list,tuple)) and isinstance(b,(list,tuple)):
            i=len(a)
            j=len(b)
            d={}
            if i>j:
                for m in range(i):
                    if m>j-1:
                        d[a[m]]=c
                    else:
                        d[a[m]]=b[m]
            else:
                for m in range(i):
                    d[a[m]]=b[m]
            return d
        else:
            return "Wrong type of input"