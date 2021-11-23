#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 12:34:17 2021

@author: akim
"""

import numpy as np
import matplotlib.pyplot as plt


dataOrig = np.genfromtxt('/home/akim/coding/data/cough/cough_inlet_velocity/time_vel.dat')

data = dataOrig
data[:,1] = data[:,1] * 0.7109110028288333

origVel1 = np.linspace(0,4.8, 150)
origVel2 = np.linspace(4.8, 0, 250)
origVel = np.concatenate((origVel1,origVel2), axis = 0)

# plt.plot(data[:, 0], origVel)
# plt.plot(data[:,0], data[:,1])

curve = data[:,1] - origVel
# plt.plot(data[:,0], curve)
fft = np.fft.fft(curve)

plt.plot(fft)
