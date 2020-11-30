#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:31:56 2020

@author: yulius
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans
from sklearn.preprocessing import  LabelEncoder

#import data
data = pd.read_csv('3.01. Country clusters.csv')

#preprocessing data
data_mapped = data.copy()
le = LabelEncoder()
data_mapped['Language'] = le.fit_transform(data_mapped['Language'])

#feature and select data
x = data_mapped.iloc[:,1:4]

#fitting cluster model KMeans
kmean = KMeans(3)
kmean.fit(x)

#predict model
identified_cluster = kmean.predict(x)
data_mapped['cluster'] =  identified_cluster

#visualisasi model
plt.scatter(data_mapped['Longitude'],data_mapped['Latitude'],c=data_mapped['cluster'],cmap='rainbow')
plt.title('KMEANS Clustering', fontsize=20)
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.show()

#wcss
#Elbow Method - Inertia plot
wcss =[]
#looping the inertia calculation for each k
for k in range(1, 7):
    #Assign KMeans as cluster_model
    cluster_model = KMeans(n_clusters = k, random_state = 24)
    #Fit cluster_model to X
    cluster_model.fit(x)
    #Get the inertia value
    inertia_value = cluster_model.inertia_
    #Append the inertia_value to inertia list
    wcss.append(inertia_value)
    
#plot inertia
plt.plot(range(1,7),wcss)
plt.title('The Elbow Method - Inertia plot', fontsize = 20)
plt.xlabel('No. of Clusters')
plt.ylabel('WCSS')
plt.show()