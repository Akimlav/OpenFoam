#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 11:37:35 2021

@author: akimlavrinenko
"""

import numpy as np
import matplotlib.pyplot as plt
import resampy
import scipy.io



mat = scipy.io.loadmat('/Users/akimlavrinenko/Downloads/signal_akim/dat.mat')

t  = mat['t'].reshape(-1)
v = mat['v'].reshape(-1)
# v = mat['v']* 0.7109110028288333
# vOrig1 = np.linspace(0,4.8, 150)
# vOrig2 = np.linspace(4.8, 0, 250)
# vOrig = np.concatenate((vOrig1, vOrig2), axis = 0)
# v = v[:,0] - vOrig

plt.plot(t,v,'k--')
plt.show()

# nr = 1
# v = resampy.resample(v, 1, nr)
# t = np.linspace(t[0]/nr,0.4,len(t)*nr)

# plt.plot(t,v,'r-')
# plt.show()

N = len(v)
a = np.fft.fft(v,axis = 0)

a = a/N

areal = np.real(a)
aimag = np.imag(a)

konda = 2 * np.pi * np.linspace(0, N-1, N)/ (max(t) - min(t))

# plt.plot(konda, areal,'o')

NH = 200
U = np.zeros((NH,N))

for k in range(0,N):
#     print(k)
    for n in range(0,int(NH/2)):
        U[n,k] = areal[n] * np.cos(2*np.pi*(n)*(k)/N) - aimag[n] * np.sin(2*np.pi*(n)*(k)/N)
    
    for n in range(int(N-NH/2), N):
        nn = int(n - (N-NH))
        U[nn,k] = areal[n] * np.cos(2*np.pi*(n)*(k)/N) - aimag[n] * np.sin(2*np.pi*(n)*(k)/N)


ondasuma = U.sum(axis=0)

plt.plot(t,v,'k--')
plt.plot(t,ondasuma, 'r-')
plt.show()