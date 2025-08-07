#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 13:03:26 2025

@author: jfrothin
"""
#import pandas as pd
import numpy as np

#%% Set up data structures - receiver ranges
# receiver data downloaded from alda (internal GBO tool)

# name: [minimum frequency in GHz, maximum frequency in GHz]
rcvr_range_ghz_dict = {}

#[name, minimum frequency in GHz, maximum frequency in GHz, prime focus or gregorian, polarization, number of beams]
rcvr_data = np.loadtxt('receivers.csv', delimiter=',', skiprows=1, max_rows=13, dtype=np.ndarray) # skip first row and last row (UWBR)

for i in range(0,len(rcvr_data)):
    rcvr_range_ghz_dict[rcvr_data[i,0]] = [float(rcvr_data[i,1]), float(rcvr_data[i,2])]

#print(rcvr_range_ghz_dict)

#%% Set up data structure - spectral windows

# would like this to mimic structure of above - read from a file rather than hardcode
# name: [center frequency in GHz, bandwidth in GHz]
spec_win_ghz_dict = {
    'HI': [1.42,0.02344],
    'test': [1.44,0.1875]#,
#    'fail': [200,1.5,42]
    }

#win_data = np.loadtxt('specwin.csv', delimiter=',',skiprows=1, dtype=np.ndarray) # issues with filetype

#%% Set up data structure - spectral lines
# name: frequency in GHz
spec_line_ghz_dict = {
    'HI 1420MHz': 1.4#,
    #'water': 22.24
    }

#%% Set up data structures - VEGAS modes
# Values from GBT Proposer's and Observer's Guides
# mode: [bandwidth in GHz, usable bandwidth, number of channels, spectral resolution in kHz, number of subbands, subband range]
vegas_modes_dict = {
    1: [1.5, 1.25, 1024, 1465.00, 1, 1.25],
    2: [1.5, 1.25, 16384, 92.00, 1, 1.25],
    3: [1.08, 0.8, 16384, 66.0, 1, 0.8],
    4: [0.1875, 0.1875, 32768, 5.70, 1, 0.1875],
    5: [0.1875, 0.1875, 65536, 2.90, 1, 0.1875],
    6: [0.1875, 0.1875, 131072, 1.40, 1, 0.1875],
    7: [0.1, 0.1, 32768, 3.1, 1, 0.1],
    8: [0.1, 0.1, 65536, 1.5, 1, 0.1],
    9: [0.1, 0.1, 131072, 0.8, 1, 0.1],
    10: [0.02344, 0.02344, 32768, 0.7, 1, 0.02344],
    11: [0.02344, 0.02344, 65536, 0.4, 1, 0.02344], 
    12: [0.02344, 0.02344, 131072, 0.2, 1, 0.02344],
    13: [0.02344, 0.02344, 262144, 0.1, 1, 0.02344],
    14: [0.02344, 0.02344, 524288, 0.04, 1, 0.02344],
    15: [0.01172, 0.01172, 32768, 0.4, 1, 0.01172],
    16: [0.01172, 0.01172, 65536, 0.2, 1, 0.01172],
    17: [0.01172, 0.01172, 131072, 0.1, 1, 0.01172], 
    18: [0.01172, 0.01172, 262144, 0.04, 1, 0.01172],
    19: [0.01172, 0.01172, 524288, 0.02, 1, 0.01172],
    20: [0.02344, 0.02344, 4096, 5.70, 8, 1.25],
    21: [0.02344, 0.02344, 8192, 2.90, 8, 1.25],
    22: [0.02344, 0.02344, 16384, 1.40, 8, 1.25],
    23: [0.02344, 0.02344, 32768, 0.70, 8, 1.25], 
    24: [0.02344, 0.02344, 65536, 0.40, 8, 1.25], 
    25: [0.0169, 0.0169, 4096, 4.10, 8, 0.8],
    26: [0.0169, 0.0169, 8192, 2.10, 8, 0.8],
    27: [0.0169, 0.0169, 16384, 1.00, 8, 0.8],
    28: [0.0169, 0.0169, 32768, 0.51, 8, 0.8],
    29: [0.0169, 0.0169, 65536, 0.26, 8, 0.8]
    } 