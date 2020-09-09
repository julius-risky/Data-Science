import pandas as pd 
from matplotlib import pyplot as plt 

df = pd.read_csv('F:\Latihan-Data-Science\statistika\Assessment_Statistics_foundation_ Dataset_superstore_simple.csv')
bawah=df['order_date']
yatas=df['sales']

df1 = bawah[:30]
df2=yatas[:30]
print(df1,df2)

#xs = [i + 0.5 for i, _ in enumerate(df2)]

plt.bar(df1, df2)

plt.xlabel('tanggal penjualan')
plt.ylabel('penjualan')

plt.title("grafik bar profit penjualan")

plt.show()