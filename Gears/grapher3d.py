#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:07:20 2018

@author: leonvillapun
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd #Libreria para importar set de datos y administrarlos

dataset = pd.read_csv('prPoints3d.csv')



fig = plt.figure()

ax1 = fig.add_subplot(111,projection='3d')



x= dataset.iloc[:,1].values
y=dataset.iloc[:,2].values
z=dataset.iloc[:,3].values

ax1.scatter(x,y,z)
ax1.set_xlabel('X');
ax1.set_ylabel('Y');
ax1.set_zlabel('Z');

plt.show()
