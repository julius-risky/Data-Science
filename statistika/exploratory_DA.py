import pandas as pd
import matplotlib.pyplot as plt

#membaca data csv
df = pd.read_csv('F:\Latihan-Data-Science\statistika\Assessment_Statistics_foundation_ Dataset_superstore_simple.csv')

#menampilkan ukuran data
print(df.shape())

#menampilkan isi data default bisi 5 data
df.head()
df.tail() # terakfir

#statistika deskriptif

print(df.describe()) #hanya numerik saja
print(df.describe(include=["object"] )) #dengan object tertentu yang tidak bernilai angka
print(df.describe(include=["ALL"] )) # semua

#menari mean,median, mode di pandas

print(df.loc[:'price'].mean()) #rata2
print(df.loc[:'price'].median())
print(df.loc[:'price'].std()) #std deviasi
print(df.loc[:'price'].var())#variansi

#histogram
order_df = pd.read_csv("order.csv")
# plot histogram kolom: price
order_df[['price']].plthist(figsize=(4, 5), bins=10, xlabelsize=8, ylabelsize=8)
plt.show()  # Untuk menampilkan histogram plot

#iqr    
#berfungsi untuk mencari pencilan
order_df = pd.read_csv("order.csv")
# Hitung quartile 1
Q1 = order_df[['product_weight_gram']].quantile(0.25)
# Hitung quartile 3
Q3 = rder_df[['product_weight_gram']].quantile(0.75)
# Hitung inter quartile range dan cetak ke console
IQR = Q3-Q1
print(IQR)

#rename columb dengan syntax
import pandas as pd
order_df = pd.read_csv("order.csv")
# Ganti nama kolom freight_value menjadi shipping_cost
order_df.rename(columns={'freight_value ': 'shipping_cost '}, inplace=True)
print(order_df)

#rename dengan indeks 
order_df.columns.values[0]="umur"

#groupby
import pandas as pd
order_df = pd.read_csv("order.csv")
# Hitung rata rata dari price per payment_type
rata_rata = order_df["price "].groupby(order_df["payment_type"]).mean()
print(rata_rata)

#sorting
order_df = pd.read_csv("order.csv")
# Hitung harga maksimum pembelian customer
sort_harga = order_df.sort_values(by="customer", ascending=False)
print(sort_harga)