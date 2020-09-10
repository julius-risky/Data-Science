name <-c('adi','burhan','samsul','ani')

#matriks

m = matrix(1:12,nrow=3)

#array
a = array(1:24,c(3,4,2))

#data frame

user <-data.frame(
  names = name,
  gender = c('male','male','male','female'),
  age = c(10,22,32,22)
)

#tipe data list

l = list(a,name,user)