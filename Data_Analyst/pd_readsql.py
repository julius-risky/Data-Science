import mysql.connector
import pandas as pd 

my_conn = mysql.connector.connect(host="localhost",
user = "root",
password = "1untuksemua",
database="toko",
use_pure=True)

my_query="""
SELECT * FROM produk;
"""
df_sql = pd.read_sql_query(my_query,my_conn)

df_sql.head()