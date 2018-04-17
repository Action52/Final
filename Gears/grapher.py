#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:07:20 2018

@author: leonvillapun
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd #Libreria para importar set de datos y administrarlos

dataset = pd.read_csv('prPoints.csv')



fig = plt.figure()

#ax1 = fig.add_subplot(111,projection='3d')



x= dataset.iloc[:,0].values
y=dataset.iloc[:,1].values
#z=dataset.iloc[:,2].values

plt.plot(x,y)


plt.show()
