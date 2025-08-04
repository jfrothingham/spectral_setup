#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 11:47:32 2025

@author: jfrothin
"""
#%% Import statements

import matplotlib.pyplot as plt
import astropy.units as u
from datetime import datetime
#import pandas as pd
import numpy as np
import os

#%% Set up data structures

rcvr_range_ghz_dict = {}

rcvr_data = np.loadtxt('receivers.csv', delimiter=',',skiprows=1, dtype=np.ndarray)

for i in range(0,len(rcvr_data)):
    rcvr_range_ghz_dict[rcvr_data[i,0]] = [float(rcvr_data[i,1]), float(rcvr_data[i,2])]

print(rcvr_range_ghz_dict)