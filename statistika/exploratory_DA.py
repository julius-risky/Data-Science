import pandas as pd
import matplotlib.pyplot as plt

#membaca data csv
df = pd.read_csv('F:\Latihan-Data-Science\statistika\Assessment_Statistics_foundation_ Dataset_superstore_simple.csv')

#menampilkan ukuran data
print(df.shape())

#menampilkan isi data default bisi 5 data
df.head()
df.tail() # terakfir

