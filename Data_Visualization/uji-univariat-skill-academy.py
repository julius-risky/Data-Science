import pandas as pd 
import statistics as stat 
from matplotlib import pyplot as plt 

#membaca file csv
df = pd.read_csv('F:\Latihan-Data-Science\statistika\Assessment_Statistics_foundation_ Dataset_superstore_simple.csv')
kolom_terpilih = df['sales']
df1=kolom_terpilih[:100]

#uji univariat/statistik deskriptif
rata2 = stat.mean(df1)
tengah = stat.median(df1)
stdv = stat.stdev(df1)
var = stat.variance(df1)

print (df1)

print('\n rata - rata dari penjualan adalah: ',rata2)
print('\n Nilai Tengah dari penjualan adalah: ',tengah)
print('\n Nilai setandar deviasi dari penjualan adalah: ',stdv)
print('\n Nilai variansi dari penjualan adalah: ',var)

#visualisasi data

xs = [ i for i, _ in enumerate(df1)]

plt.plot(xs, df1,'g-',label='sales')
plt.legend(loc='best')

plt.xlabel('Penjualan')
plt.title('Grafik penjualan')
plt.show()