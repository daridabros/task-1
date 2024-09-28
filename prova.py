import pandas as pd
import csv
from matplotlib import pyplot as plt

import numpy as np

# Apertura e lettura file CSV
df = pd.read_csv('Amazon_Sales_data.csv')
#display(df)

print(f"The number of NaN for each column are: \n{df.isna().sum()}")
df = df.dropna()
pd.options.display.float_format = '{:.2f}'.format

print(f"{df.describe()}")

import datetime

#Normalizzato i campi "Order Date" e "Ship Date" trasfromandoli in Date e poi ordino il Dataframe in ordine di data.
df["Order Date"] = pd.to_datetime(df["Order Date"].str.replace("-", "/"), format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"].str.replace("-", "/"), format="%m/%d/%Y")
df = df.sort_values("Order Date")

def vendite_anno_mese(df):
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Year-Month"] = df["Year"].astype(str) + "-" + df["Month"].astype(str).str.zfill(2)
    
    
    risultato = df.groupby(["Year-Month", "Month", "Year"])["Units Sold"].sum().reset_index()
    # print(risultato)
    return risultato

df_anno_mese = vendite_anno_mese(df)

#Ordino per mese
df_anno_mese = df_anno_mese.sort_values("Month")

# Ottieni i dati da df_anno_mese
x = df_anno_mese["Month"].values       # Asse x: Mese
y = df_anno_mese["Year"].values        # Asse y: Anno
z = np.zeros_like(x)                   # Asse z: Tutte le barre iniziano da zero
dx = np.ones_like(x) * 0.5             # Larghezza delle barre in x
dy = np.ones_like(y) * 0.5             # Larghezza delle barre in y
dz = df_anno_mese["Units Sold"].values # Altezza delle barre (Units Sold)

# Creazione del grafico 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Creazione delle barre 3D
ax.bar3d(x, y, z, dx, dy, dz, color='skyblue', edgecolor='black', alpha=0.7)

# Etichette e titolo
ax.set_xlabel('Month')
ax.set_ylabel('Year')
ax.set_zlabel('Units Sold')
ax.set_title('Monthly Units Sold Over Years')

# Imposta i tick labels per l'asse x e y
ax.set_xticks(np.arange(1, 13))  # Mesi da 1 a 12
ax.set_yticks(sorted(df_anno_mese["Year"].unique()))  # Anni presenti nei dati

plt.show()