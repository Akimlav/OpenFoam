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


dirPath = '/Users/akimlavrinenko/Documents/coding/data/cough/mesh_conv'

foldName = 'pure_cloud_data'

folders = openFoam().fast_scandir(dirPath)
folders = [word for word in folders if foldName in word]
folders.sort()
listOfFileList, allFileList = openFoam().listfile(folders, '.dat')
allFileList.sort()
#calculations
firstMomentList = []
#[time, xRange, yRange, zRange, T, xT, yT, zT, 
# x2T, y2T, z2T, dimT, xDimT, yDimT, zDimT, x2DimT, y2DimT, z2DimT]
fontP = FontProperties()
fontP.set_size('xx-small')
fig, axs = plt.subplots(8, figsize=(5, 15))
for i in range(len(allFileList)):
    print(allFileList[i])
    data=np.genfromtxt(folders[0] + '/' + allFileList[i], invalid_raise = False)
    axs[0].plot(data[:,0], data[:,1] ,label = allFileList[i])
    axs[0].set_title('x range')
    axs[0].grid(True)
    axs[0].set_xlim(0,1.5)
    axs[0].set_xlabel('time [s]')
    axs[0].set_ylabel('[m]')
    
    axs[1].plot(data[:,0], data[:,2])
    axs[1].plot(data[:,0], data[:,1], '--')
    axs[1].set_title('z range')
    axs[1].grid(True)
    axs[1].set_xlim(0,1.5)
    axs[1].set_ylim(0,0.3)
    axs[1].set_xlabel('time [s]')
    axs[1].set_ylabel('[m]')
    
    
    firstXm = data[:,5] / data[:,4]
    firstDimXm = data[:,13] / data[:,12]
    
    axs[2].plot(data[:,0], firstXm)
    axs[2].plot(data[:,0], firstDimXm, '--')
    axs[2].set_title('first X moment')
    axs[2].grid(True)
    axs[2].set_xlim(0,1.5)
    axs[2].set_xlabel('time [s]')
    axs[2].set_ylabel('[m]')
    firstYm = data[:,6] / data[:,4]
    
    axs[3].plot(data[:,0], firstYm)
    axs[3].set_title('first Y moment')
    axs[3].grid(True)
    axs[3].set_xlim(0,1.5)
    axs[3].set_xlabel('time [s]')
    axs[3].set_ylabel('[m]')
    firstZm = data[:,7] / data[:,4]
    
    axs[4].plot(data[:,0], firstZm)
    axs[4].set_title('first Z moment')
    axs[4].grid(True)
    axs[4].set_xlim(0,1.5)
    axs[4].set_ylim(0,0.05)
    axs[4].set_xlabel('time [s]')
    axs[4].set_ylabel('[m]')
    secondXm = data[:,8] / data[:,4]

    
    axs[5].plot(data[:,0], secondXm)
    axs[2].plot(data[:,0], firstDimXm, '--')
    axs[5].set_title('second X moment')
    axs[5].grid(True)
    axs[5].set_xlim(0,1.5)
    axs[5].set_xlabel('time [s]')
    axs[5].set_ylabel('[m]')
    secondYm = data[:,9] / data[:,4]
    
    axs[6].plot(data[:,0], secondYm)
    axs[6].set_title('second Y moment')
    axs[6].grid(True)
    axs[6].set_xlim(0,1.5)
    axs[6].set_ylim(0,0.002)
    axs[6].set_xlabel('time [s]')
    axs[6].set_ylabel('[m]')
    secondZm = data[:,10] / data[:,4]
    
    axs[7].plot(data[:,0], secondZm)
    axs[7].set_title('second Z moment')
    axs[7].grid(True)
    axs[7].set_xlim(0,1.5)
    axs[7].set_ylim(0,0.0075)
    axs[7].set_xlabel('time [s]')
    axs[7].set_ylabel('[m]')
    axs[2].set_ylim(0,0.3)
    firstMomentList.append([data[:,0], firstXm, firstZm])
fig.suptitle('plume data', fontsize=14)
fig.tight_layout()
fig.legend(title='mesh', bbox_to_anchor=(0.15, 0.97), loc='upper left', prop=fontP)
# plt.savefig('mesh_plume_data.png', dpi=150)
# plt.show()
    
t = 1.5
cells = [178000, 510000, 1000000, 3000000, 5000000, 10000000, 17000000]
fmList_1_5 = []
smList_1_5 = []
rangeList_1_5 = []

for i in range(len(allFileList)):
    data=np.genfromtxt(folders[0] + '/' + allFileList[i], invalid_raise = False)
    ind = np.where(data[:,0] == t)

    firstXm = data[ind[0],5] / data[ind[0],4]
    firstYm = data[ind[0],6] / data[ind[0],4]
    firstZm = data[ind[0],7] / data[ind[0],4]
    secondXm = data[ind[0],8] / data[ind[0],4]
    secondYm = data[ind[0],9] / data[ind[0],4]
    secondZm = data[ind[0],10] / data[ind[0],4]
    fmList_1_5.append([cells[i], firstXm[0], firstYm[0], firstZm[0]])
    smList_1_5.append([cells[i], secondXm[0], secondYm[0], secondZm[0]])
    rangeList_1_5.append([int(cells[i]), data[ind[0],2], data[ind[0],3], data[ind[0],1]])

fmList_1_5 = np.asarray(fmList_1_5)
smList_1_5 = np.asarray(smList_1_5)
rangeList_1_5 = np.asarray(rangeList_1_5)

fig, axs = plt.subplots(2, figsize=(5, 7))

axs[0].plot(rangeList_1_5[:,0], rangeList_1_5[:,3], 'ko-', label = 'range')
axs[0].plot(fmList_1_5[:,0], fmList_1_5[:,1], 'bo-',label = 'centroid')
axs[0].plot(smList_1_5[:,0], smList_1_5[:,1], 'ro-', label = 'variance')
# axs[0].plot(fmList_1_5[:,0], fmList_1_5[:,2],'o-', label = 'y')
# axs[0].plot(fmList_1_5[:,0], fmList_1_5[:,3],'o-', label = 'z')
# axs[0].set_xscale('log')
axs[0].set_title('axis X')
axs[0].set_xlabel('cells')
axs[0].set_ylabel('[m]')
axs[0].grid(True)


axs[1].plot(rangeList_1_5[:,0], rangeList_1_5[:,1],'ko-')
axs[1].plot(fmList_1_5[:,0], fmList_1_5[:,3],'bo-')
axs[1].plot(smList_1_5[:,0], smList_1_5[:,3],'ro-')
axs[1].set_title('axis Z')
axs[1].set_xlabel('cells')
axs[1].set_ylabel('[m]')
axs[1].grid(True)


# np.savetxt('range.dat', rangeList_1_5)
# np.savetxt('fm.dat', fmList_1_5)
# np.savetxt('sm.dat', smList_1_5)

# axs[2].plot(rangeList_1_5[:,0], rangeList_1_5[:,3], 'o-')
# axs[2].plot(rangeList_1_5[:,0], rangeList_1_5[:,3],'o-')
# axs[2].plot(rangeList_1_5[:,0], rangeList_1_5[:,3],'o-')
# axs[2].set_title('axi Z')
# axs[2].set_ylabel('[m]')
# axs[2].set_xlabel('cells')
# axs[2].grid(True)
fig.suptitle('puff data '+ str(t) + ' [s]' , fontsize=14)
fig.tight_layout()
fig.legend(title = 'cloud', bbox_to_anchor=(0.75, 0.88), loc='upper left', prop=fontP)
# plt.savefig('mesh_conv_data_' + str(t) + '.png', dpi=150)
plt.show()

for i in range(len(allFileList)):
    dd = np.asarray(firstMomentList[i]).T
    # np.savetxt('cloud_' + str(cells[i]) + '.dat', dd)
    
