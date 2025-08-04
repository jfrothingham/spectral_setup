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

#%% Set up data structures - receiver ranges
# receiver data downloaded from https://alda.gb.nrao.edu/receiver/receivers (internal GBO tool)

rcvr_range_ghz_dict = {}

rcvr_data = np.loadtxt('receivers.csv', delimiter=',',skiprows=1, dtype=np.ndarray)

for i in range(0,len(rcvr_data)):
    rcvr_range_ghz_dict[rcvr_data[i,0]] = [float(rcvr_data[i,1]), float(rcvr_data[i,2])]

#print(rcvr_range_ghz_dict)

#%% Set up data structures - VEGAS modes
 # to do later - will need to pull values from GBT Proposer's and Observer's Guides

#%% Plotting

toplot = ['Rcvr1_2', 'Rcvr2_3', 'Rcvr4_6']

#toplot = rcvr_range_ghz_dict.keys()

fig, ax1 = plt.subplots()
ax1.set_xlabel('Frequecy in GHz')
ax1.set_xscale('log')
ax1.set_ylabel('arbitrary units')

i=0
for rcvr in toplot:
    x1, x2 = rcvr_range_ghz_dict[rcvr]
    bw = x2-x1
    #ax1.fill_betweenx([0,1], x1, x2, label=rcvr)
    #ax1.plot([x1,x2], [0, 0], label=rcvr)
    #ax1.text(x1, 0, rcvr)
    
    ax1.vlines([x1, x2], [0,0], [1,1],ls='--',color='k',alpha=0.5)
    ax1.text((bw/2)+x1, 0, rcvr, ha='center')
    
    i+=1

ax1.plot()
#ax1.legend()
