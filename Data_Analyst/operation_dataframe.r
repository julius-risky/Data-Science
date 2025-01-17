dataset <- read.csv('Assessment_Statistics_foundation_ Dataset_superstore_simple.csv')

nrow(dataset)
ncol(dataset)
#memilih data
dr <- select(dataset,-c(order_id)) #-c() untuk memilih kecuali kolom tersebut
#memfilter data
dr<- filter(dataset, segment=='Consumer' & profit >0)

# & dan
#| or

#mutate 
#membuat kolom baru
dr<-mutate(dataset,avg_price = sales/quantity)

#transmut
#melihat kolom baru saja
dr<-transmute(dataset,avg_price = sales/quantity)

