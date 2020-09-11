library(dplyr)
library(ggplot2)

dataset <- read.csv('Assessment_Statistics_foundation_ Dataset_superstore_simple.csv')

plot1<-ggplot(dataset,aes(x=sales,y=profit))+
  geom_point(aes(color=category),size=1,shape=16) +
  geom_smooth(method='lm',color='black',linetype='dotdash',size=1)+
  labs(title = 'Scater plot sales vs profit',
       subtitle = 'Based on dataset superstore',
       caption = 'R language tutorial')+
    xlab('order sale')+
    ylab('order profit')+
  theme(
    plot.title = element_text(color='blue',size=15,face='bold'),
    plot.subtitle = element_text(color='black',size=12,face='italic')
  )
plot2 <- plot1+  theme(
  legend.position=c(0.8,0.3),
  legend.title = element_text(color='blue',size=12,face='bold'),
  legend.text = element_text(size=10,color='red'),
)

plot2

ggsave(plot2,'tes.png')