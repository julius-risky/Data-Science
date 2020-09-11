library(dplyr)
library(ggplot2)

dataset <- read.csv('Assessment_Statistics_foundation_ Dataset_superstore_simple.csv')
#visualisasi sccater plot

ggplot(dataset,aes(x=sales,y =profit))+geom_point(colour='blue')

#visualisasi histogram

ggplot(dataset,aes(sales))+geom_histogram(bins =10)

#bar chart

ggplot(dataset,aes(x=segment,y=sales)) + geom_bar(stat = 'identity', width=0.5,aes(fill=category))

