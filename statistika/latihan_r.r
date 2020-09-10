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

#membuat fungsi 2 variable
Lsegitiga <- function(alas,tinggi){
  luas1 <-(1/2*alas*tinggi)
  return(luas1)
}

hw <- function(){
  print('hello word')
}

berhitung <- function(n){
  for(i in 1:n){
  print(i)}
  }