a<- -5
b<-5.7

if(a==19){
  print('ini adalah angka sepuluh')
} else{
  print('ini bukan sepuluh')
}

if(a==10){
  print('ini adalah angka sepuluh')
} else if(a>0){
  print('a adalah angka positif')
} else{
  print('a bukan angka positif')
}

i <- 1
while(i<10){
  print(i*i)
  i<-i+1
}

for (i in name) {
print(paste('haloo',i))  
}

Llingkaran <- function(r){
  pi <-3.14
  luas <- pi*r^2
  return(luas)
}
