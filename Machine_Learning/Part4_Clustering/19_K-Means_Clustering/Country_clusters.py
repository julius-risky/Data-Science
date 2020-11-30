#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 23:53:20 2020

@author: yulius
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

#import data
data = pd.read_csv('3.01. Country clusters.csv') 

#plot data
plt.title('Plot data')
plt.scatter(data['Longitude'],data['Latitude'])
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.show

#feature selection
x = data.iloc[:, 1:3]

#clustering model
kmean = KMeans(3)
kmean.fit(x)

#predict
identified_cluster = kmean.predict(x)

data_with_cluster = data.copy()
data_with_cluster['Cluster'] = identified_cluster

#plot cluster

plt.scatter(data_with_cluster['Longitude'],data_with_cluster['Latitude'],
            c=data_with_cluster.Cluster, cmap='rainbow')
plt.title('Plot with cluster')
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.show
