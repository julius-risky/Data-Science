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
