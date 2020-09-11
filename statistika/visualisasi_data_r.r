library(dplyr)
library(ggplot2)

dataset <- read.csv('Assessment_Statistics_foundation_ Dataset_superstore_simple.csv')
#visualisasi sccater plot

ggplot(dataset,aes(x=sales,y =profit))+geom_point(colour='blue')

