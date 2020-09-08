import pandas as pd 
from matplotlib import pyplot as plt 

df = pd.read_csv('F:\Data science\Latihan statistika\Assessment Statistics foundation_ Dataset_superstore_simple.csv')
kolom_terpilih = df['sales']
df1=kolom_terpilih[:100]

xs = [ i for i, _ in enumerate(df1)]

plt.plot(xs, df1,'g-',label='sales')

plt.legend(loc='best')

plt.xlabel('Periode penjualan')
plt.ylabel('Frekuensi')
plt.title('Grafik penjualan')
plt.show()
print(df1)