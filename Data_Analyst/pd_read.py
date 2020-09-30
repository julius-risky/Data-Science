import pandas as pd
# File CSV
df_csv = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")
print(df_csv.head(3)) # Menampilkan 3 data teratas
# File TSV
df_tsv = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_tsv.tsv", sep='\t')
print(df_tsv.head(3)) # Menampilkan 3 data teratas

# File xlsx dengan data di sheet "test"
df_excel = pd.read_excel("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_excel.xlsx", sheet_name="test")
print(df_excel.head()) # Menampilkan 4 data teratas

# File JSON
url = "https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/covid2019-api-herokuapp-v2.json"
df_json = pd.read_json(url)
print(df_json.head()) # Menampilkan 10 data teratas