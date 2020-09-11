library(dplyr)
library(ggplot2)

dataset <- read.csv('Assessment_Statistics_foundation_ Dataset_superstore_simple.csv')
#visualisasi sccater plot

ggplot(dataset,aes(x=sales,y =profit))+geom_point(colour='blue')

#visualisasi histogram

ggplot(dataset,aes(sales))+geom_histogram(bins =10)

#bar chart

ggplot(dataset,aes(x=segment,y=sales)) + geom_bar(stat = 'identity', width=0.5,aes(fill=category))

#pie chart

sales_per_segment<- dataset %>%group_by(segment) %>% summarise(total_sales=sum(sales))
ggplot(sale#pie chart

sales_per_segment<- dataset %>%group_by(segment) %>% summarise(total_sales=sum(sales))
ggplot(sales_per_segment,aes(x='',y=total_sales,fill=segment)) + geom_bar(stat='identity',width = 5)+coord_polar('y',start=0)

#line chart
dataset$order_date <-as.Date(dataset$order_date)
dataset$order_month <- as.Date(cut(dataset$order_date, breaks = 'month'))

ggplot(dataset, aes(x= order_month,y=sales))+stat_summary(fun.y = sum,geom='line')

mount_sales <- dataset%>% group_by(order_month)%>%summarise(sales=sum(sales))

ggplot(mount_sales,aes(x=order_month,y=sales)) + geom_line()+geom_point(colour='blue')