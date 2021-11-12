#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:17:58 2021

@author: akimlavrinenko
"""
from openFoamClass import openFoam
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


dirPath = '/media/HDD/FOAM/cough/mesh_conv/'

foldName = 'plume_data'

folders = openFoam().fast_scandir(dirPath)
folders = [word for word in folders if foldName in word]
folders.sort()
listOfFileList, allFileList = openFoam().listfile(folders, '.txt')
allFileList.sort()
#calculations

#[time, xRange, yRange, zRange, T, xT, yT, zT, 
# x2T, y2T, z2T, dimT, xDimT, yDimT, zDimT, x2DimT, y2DimT, z2DimT]
fontP = FontProperties()
fontP.set_size('xx-small')
fig, axs = plt.subplots(8, figsize=(5, 15))
for i in range(len(allFileList)):
    data=np.genfromtxt(folders[0] + '/' + allFileList[i], invalid_raise = False)
    axs[0].plot(data[:,0], data[:,1] ,label = allFileList[i])
    axs[0].set_title('x range')
    axs[0].grid(True)
    axs[0].set_xlim(0,1.5)
    
    axs[1].plot(data[:,0], data[:,2])
    # axs[1].plot(data[:,0], data[:,1], '--')
    axs[1].set_title('z and y range')
    axs[1].grid(True)
    axs[1].set_xlim(0,1.5)
    axs[1].set_ylim(0,0.3)
    
    
    firstXm = data[:,5] / data[:,4]
    firstDimXm = data[:,13] / data[:,12]
    
    axs[2].plot(data[:,0], firstXm)
    # axs[2].plot(data[:,0], firstDimXm, '--')
    axs[2].set_title('first X moment')
    axs[2].grid(True)
    axs[2].set_xlim(0,1.5)
    
    firstYm = data[:,6] / data[:,4]
    
    axs[3].plot(data[:,0], firstYm)
    axs[3].set_title('first Y moment')
    axs[3].grid(True)
    axs[3].set_xlim(0,1.5)
    
    firstZm = data[:,7] / data[:,4]
    
    axs[4].plot(data[:,0], firstZm)
    axs[4].set_title('first Z moment')
    axs[4].grid(True)
    axs[4].set_xlim(0,1.5)
    axs[4].set_ylim(0,0.05)
    
    secondXm = data[:,8] / data[:,4]

    
    axs[5].plot(data[:,0], secondXm)
    # axs[2].plot(data[:,0], firstDimXm, '--')
    axs[5].set_title('second X moment')
    axs[5].grid(True)
    axs[5].set_xlim(0,1.5)
    
    secondYm = data[:,9] / data[:,4]
    
    axs[6].plot(data[:,0], secondYm)
    axs[6].set_title('second Y moment')
    axs[6].grid(True)
    axs[6].set_xlim(0,1.5)
    axs[6].set_ylim(0,0.002)
    
    secondZm = data[:,10] / data[:,4]
    
    axs[7].plot(data[:,0], secondZm)
    axs[7].set_title('second Z moment')
    axs[7].grid(True)
    axs[7].set_xlim(0,1.5)
    axs[7].set_ylim(0,0.0075)
    
    # axs[2].set_ylim(0,0.3)
    
fig.suptitle('plume data', fontsize=14)
fig.tight_layout()
fig.legend(title='mesh', bbox_to_anchor=(0.15, 0.97), loc='upper left', prop=fontP)
plt.savefig('mesh_plume_data.png', dpi=150)
plt.show()
    

fig, axs = plt.subplots(8, figsize=(5, 10))
for i in range(len(allFileList)):
    data=np.genfromtxt(folders[0] + '/' + allFileList[i], invalid_raise = False)
    axs[0].plot(data[:,0], data[:,1] ,label = allFileList[i])
    axs[0].set_title('x range')
    axs[0].grid(True)
    axs[0].set_xlim(0,1.5)
    