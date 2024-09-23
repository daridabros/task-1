import pandas as pd
import csv
from matplotlib import pyplot as plt

# Apertura e lettura file CSV
df = pd.read_csv('Amazon_Sales_data.csv')
#display(df)

print(f"The number of NaN for each column are: \n{df.isna().sum()}")
df = df.dropna()
pd.options.display.float_format = '{:.2f}'.format

print(f"{df.describe()}")

import datetime

#Normalizzato i campi "Order Date" e "Ship Date" trasfromandoli in Date e poi ordino il Dataframe in ordine di data.
df["Order Date"] = df["Order Date"].str.replace("-", "/")
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = df["Ship Date"].str.replace("-", "/")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")
df = df.sort_values("Order Date")

def calcola_vendite_mensili(df):
    # Creiamo un dizionario per memorizzare i totali delle vendite
    vendite_mensili = {}
    
    # Aggiungiamo una colonna per l'anno-mese
    df['Anno-Mese'] = df['Order Date'].dt.to_period('M')
    
    # Raggruppiamo per Anno-Mese e contiamo le transazioni
    conteggio_mensile = df.groupby('Anno-Mese').size()
    
    # Iteriamo sui risultati e popoliamo il dizionario
    for periodo, conteggio in conteggio_mensile.items():
        chiave = f"{periodo.year}-{periodo.month:02d}"
        vendite_mensili[chiave] = conteggio
    
    return vendite_mensili

# Utilizziamo la funzione sul nostro DataFrame
risultato_vendite = calcola_vendite_mensili(df)

# Creiamo un DataFrame per i risultati
df_vendite = pd.DataFrame(list(risultato_vendite.items()), columns=['Anno-Mese', 'Vendite'])

print(df_vendite)


        
        


   
     

