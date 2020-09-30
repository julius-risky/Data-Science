import mysql.connector
import pandas as pd 

my_conn = mysql.connector.connect(host="localhost",
user = "root",
password = "1untuksemua",
database="toko",
use_pure=True)
