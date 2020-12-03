#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:48:05 2020

@author: yulius
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#imprt data
data = pd.read_csv('Country clusters standardized.csv', index_col='Country')

X_scaled = data.copy()
X_scaled = X_scaled.drop(['Language'],axis=1)

sns.clustermap(X_scaled, cmap ='mako')
