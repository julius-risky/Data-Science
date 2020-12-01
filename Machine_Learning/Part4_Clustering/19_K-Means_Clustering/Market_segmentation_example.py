#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:28:47 2020

@author: yulius
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Set the styles to Seaborn
sns.set()
# Import the KMeans module so we can perform k-means clustering with sklearn
from sklearn.cluster import KMeans 
from sklearn.preprocessing import scale

#import data 
data = pd.read_csv('3.12. Example.csv')

#plot data
plt.scatter(data['Satisfaction'],data['Loyalty'])
plt.title('plot market segmentation',fontsize=20 )
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')

#feature
x = data.copy()

#clustering
kmean= KMeans(2)
kmean.fit(x)

#cluster result
clus=x.copy()
clus['Cluster_result']=kmean.predict(x)

#plot result
plt.scatter(clus['Satisfaction'],clus['Loyalty'],c=clus['Cluster_result'],cmap='rainbow')
plt.title('Cluster result market segmentation' ,fontsize=20)
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')

#standarization
x_scale = scale(x)

#elbow methode
wcss= []
for i in range (1,10):
    kmean= KMeans(i)
    kmean.fit(x_scale)
    wcss.append(kmean.inertia_)
 
#plot elbow method

plt.plot(range(1,10),wcss) 
# Name your axes
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')

# Explore clustering solution

kmean_new = KMeans(2)
kmean_new.fit(x_scale)
cluster_new = x.copy()
cluster_new['New_cluster']= kmean_new.predict(x_scale)

#new plot result
plt.scatter(cluster_new['Satisfaction'],cluster_new['Loyalty'],c=cluster_new['New_cluster'],cmap='rainbow')
plt.title('Cluster result market segmentation after scaling' ,fontsize=20)
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')
