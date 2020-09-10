dataset <- read.csv('Assessment_Statistics_foundation_ Dataset_superstore_simple.csv')

nrow(dataset)
ncol(dataset)
#memfilter data
dr<- filter(dataset, segment=='Consumer' & profit >0)

# & dan
#| or

