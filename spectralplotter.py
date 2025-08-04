#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 11:47:32 2025

@author: jfrothin
"""

# import a frequency setup
try: 
    from freqsetup import spec_dict_GHz
except:
    spec_dict = {"none":{}}

import matplotlib.pyplot as plt
import astropy.units as u
from datetime import datetime
import numpy as np
import os
