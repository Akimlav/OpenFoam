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


dirPath1 = '/Users/akimlavrinenko/Documents/coding/data/cough/DNS_cough_data/'
dirPath2 = '/Users/akimlavrinenko/Documents/coding/data/cough/RANS_cough_data/'
dirPath3 = '/Users/akimlavrinenko/Documents/coding/data/cough/LES_cough_data/'

cloud1 = np.genfromtxt(dirPath2 + '1kk_cloud.dat')
# cloud1b = np.genfromtxt(dirPath2 + '1kkb_cloud.dat')
# cloud10 = np.genfromtxt(dirPath2 + '10kk_cloud.dat')
cloud17 = np.genfromtxt(dirPath2 + '17kk_cloud.dat')
cloudDns = np.genfromtxt(dirPath1 + 'DNS_centroid_variance.dat')
cloudLes = np.genfromtxt(dirPath3 + 'case2_LES.dat')


dirPath = '/Users/akimlavrinenko/Documents/coding/data/cough/mesh_conv'

foldName = 'pure_cloud_data'


#[time, xRange, yRange, zRange, T, xT, zT, xxT, zzT, xc, zc, sigmaX, sigmaZ]
fontP = FontProperties()
fontP.set_size('xx-small')
fig, axs = plt.subplots(2, figsize=(5, 8))
axs[0].plot(cloudDns[:,1], cloudDns[:,0] ,'k--', label='DNS')
axs[0].plot(cloudLes[:,9], cloudLes[:,0] ,'r--', label='LES 2.5kk')
axs[0].plot(cloud1[:,1], cloud1[:,0] ,'b--', label='RANS 1kk')
axs[0].plot(cloud17[:,1], cloud17[:,0] ,'c--', label='RANS 17kk')
axs[0].legend()

axs[0].set_title('centroid horizontal')
axs[0].grid(True)
# axs[0].set_xlim(0,1)
axs[0].set_xlabel('x m')
axs[0].set_ylabel('t, s')

axs[1].plot(cloudDns[:,2], cloudDns[:,0] ,'k--', label='DNS')
axs[1].plot(cloudLes[:,10], cloudLes[:,0] ,'r--', label='LES 2.5kk')
axs[1].plot(cloud1[:,2], cloud1[:,0] ,'b--', label='RANS 1kk')
axs[1].plot(cloud17[:,2], cloud17[:,0] ,'c--', label='RANS 17kk')
axs[1].set_title('centroid vertical')
axs[1].grid(True)
# axs[1].set_xlim(0,0.8)

axs[1].set_xlabel('z m')
axs[1].set_ylabel('t, s')



fig.tight_layout()
# fig.legend(title='mesh', bbox_to_anchor=(0.15, 0.97), loc='upper left', prop=fontP)
plt.savefig('DNS_LES_puff_data.png', dpi=150)
plt.show()

fig, axs = plt.subplots(2, figsize=(5, 8))
axs[0].plot(cloudDns[:,1], cloudDns[:,0] ,'k--', label='DNS')
axs[0].plot(cloudLes[:,9], cloudLes[:,0] ,'r--', label='LES 2.5kk')
axs[0].plot(cloud1[:,1], cloud1[:,0] ,'b--', label='RANS 1kk')
axs[0].plot(cloud17[:,1], cloud17[:,0] ,'c--', label='RANS 17kk')
axs[0].legend()

axs[0].set_title('centroid horizontal')
axs[0].grid(True)
# axs[0].set_xlim(0,1)
axs[0].set_xlabel('x m')
axs[0].set_ylabel('t, s')

axs[1].plot(cloudDns[:,2], cloudDns[:,0] ,'k--', label='DNS')
axs[1].plot(cloudLes[:,10], cloudLes[:,0] ,'r--', label='LES 2.5kk')
axs[1].plot(cloud1[:,2], cloud1[:,0] ,'b--', label='RANS 1kk')
axs[1].plot(cloud17[:,2], cloud17[:,0] ,'c--', label='RANS 17kk')
axs[1].set_title('centroid vertical')
axs[1].grid(True)
# axs[1].set_xlim(0,0.8)

axs[1].set_xlabel('z m')
axs[1].set_ylabel('t, s')



fig.tight_layout()
# fig.legend(title='mesh', bbox_to_anchor=(0.15, 0.97), loc='upper left', prop=fontP)
# plt.savefig('DNS_LES_puff_data.png', dpi=150)
plt.show()