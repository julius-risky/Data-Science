import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.colors as mcolors

# ngebaca data csv 
df = pd.read_csv('F:\Latihan-Data-Science\statistika\Assessment_Statistics_foundation_ Dataset_superstore_simple.csv')
# https://data.go.id/

# buat nampilin biar full tulisannya
# pd.set_option('display.max_colwidth', None)

# buat reset ke tampilan semula
pd.reset_option('^display.', silent=True)

# df.head(2)

# hanya menampilkan beberapa kolom
# lala = df[['Penyakit','Jumlah']]

#nampilin berapa yang mau ditampilin
df1=df[:10] 

# sort
# df.sort_values(by=['Jumlah'], inplace=True, ascending=False)

# Dropping old Name columns 
# ngehapus kolom
# df.drop(columns =["Jumlah"], inplace = True) 

print(df1)

# Create a list of colors (from iWantHue)
colors = random.choices(list(mcolors.CSS4_COLORS.values()),k = 15)

# Create a list of colors (from theme)
# https://www.pythonprogramming.in/how-to-pie-chart-with-different-color-themes-in-matplotlib.html
theme = plt.get_cmap('hsv')
# 1 * perulangan dari len si jumlah tu
colors = [theme(1. * i / len(df1['Jumlah']))
                             for i in range(len(df1['Jumlah']))]

# Create a pie chart
plt.pie(
    # using data total)arrests
    df1['Jumlah'],
    # with the labels being officer names
    # labels=df1['Penyakit'],
    # with no shadows
    shadow=False,
    # with colors
    colors=colors,
    # with the start angle at 90%
    startangle=90,
    # with the percent listed as a fraction
    autopct='%.1f%%',
)
total = sum(df1['Jumlah'])

# View the plot drop above
plt.axis('equal')

# View the plot
# plt.tight_layout()
plt.title("10 Penyakit teratas di Puskesmas Kota Bandung Tahun 2017")
plt.legend(
    # lokasi awal si pie
    loc='upper left',
    labels=['%s, %1.1f%%' % (
        l, (float(s) / total) * 100) for l, s in zip(df1['Penyakit'], df1['Jumlah'])],
    prop={'size': 11},
    # kek yang di word image tu (x, y, width, height)
    bbox_to_anchor=(1, 0.6),
    bbox_transform=fig1.transFigure
)
plt.show()