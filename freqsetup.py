#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 13:03:26 2025

@author: jfrothin
"""
#import pandas as pd
import numpy as np

spec_dict_GHz = {'none':{}, 'receivers': {}}

rcvr_data = np.loadtxt('receivers.csv', delimiter=',',skiprows=1, dtype=np.ndarray)

for i in range(0,len(rcvr_data)):
    spec_dict_GHz['receivers'][rcvr_data[i,0]] = [float(rcvr_data[i,1]), float(rcvr_data[i,2])]

print(spec_dict_GHz['receivers'])