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

# this is messy!!! restructure code to use actual package/module convention
from freqsetup import *

#%% Define function to determine receiver from spectral window
def rcvr_select(specwin_dict, rcvr_dict):
    """
    Determine corresponding receiver(s) from list of spectral windows
    
    Parameters
    ----------
    specwin_dict : dict
        DESCRIPTION.
    rcvr_dict : dict
        DESCRIPTION.

    Returns
    -------
    rcvr_return : dict
        Dictionary of unique receivers that the provided spectral windows fall within

    """
    rcvr_return = {}
    
    for entry in specwin_dict.keys():
        cf = specwin_dict[entry][0]
        failure=True
        for rcvr in rcvr_dict.keys():
            rxlow, rxhi = rcvr_dict[rcvr]
            if cf > rxlow and cf < rxhi:
                failure=False
                if rcvr not in rcvr_return.keys(): rcvr_return[rcvr] = rcvr_dict[rcvr]
                
        if failure is True:
            print("uh oh! spectral window", entry, " with central frequency", cf, "GHz is not within any known receiver range")
            
    return rcvr_return

#%% Define custom plotting method
def plot_obs(ax, plot_rcvr=True, rcvr_dict="none", plot_spect=True, specwind_dict="none", plot_line=True, line_dict="none", legend=True, ploty=1):
    """
    

    Parameters
    ----------
    ax : TYPE
        DESCRIPTION.
    plot_rcvr : TYPE, optional
        DESCRIPTION. The default is True.
    rcvr_dict : TYPE, optional
        DESCRIPTION. The default is "none".
    plot_spect : TYPE, optional
        DESCRIPTION. The default is True.
    specwind_dict : TYPE, optional
        DESCRIPTION. The default is "none".
    plot_line : TYPE, optional
        DESCRIPTION. The default is True.
    line_dict : TYPE, optional
        DESCRIPTION. The default is "none".

    Returns
    -------
    None.

    """
    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = prop_cycle.by_key()['color']
    
    if plot_spect:
        if specwind_dict == "none":
            print("No spectral windows to plot")
        else:
            i=0
            for entry in specwind_dict:
                c = colors[i]
                cf, bw = specwind_dict[entry]
                wx1 = cf - (0.5*bw)
                wx2 = cf + (0.5*bw)
                ax.fill_between([wx1, wx2],[ploty,ploty], alpha=0.5)
                #ax.plot([wx1,wx2], [ploty/2, ploty/2], color=c, label=entry)
                ax.vlines(cf, 0, ploty, ls='--', color=c, label=entry)
                i+=1
        
    if plot_rcvr:
        if rcvr_dict == "none":
            print("No receiver ranges to plot")
        else:
            for rx in rcvr_dict:
                rx1, rx2 = rcvr_range_ghz_dict[rx]
                rxbw = rx2-rx1
                ax.vlines([rx1, rx2], [0,0], [ploty,ploty], ls='--',color='k',alpha=0.75)
                ax.text(rx1, 0, rx)
                
    if plot_line:
        if line_dict == "none":
            print("No spectral lines to plot")
            
        else:
            for line in line_dict:
                l1 = line_dict[line]
                ax.vlines(l1, 0, ploty, label=line)
                
    if legend:
        ax.legend()
        
    return

 #%%% Scratch work

fig, ax1 = plt.subplots()
ax1.set_xlabel('Frequecy in GHz')
#ax1.set_xscale('log')
ax1.set_ylabel('arbitrary units')

rcvrs = rcvr_select(spec_win_ghz_dict, rcvr_range_ghz_dict)

plot_obs(ax1, plot_rcvr=True, rcvr_dict=rcvrs, plot_spect=True, specwind_dict=spec_win_ghz_dict, plot_line=True, line_dict=spec_line_ghz_dict)
