import pandas as pd
import numpy as np
df = pd.read_csv("D:\Documentos\GitHub\Proyectos-Luis\chipotle.tsv", sep="\t")
print(df.head(5))
lista = list()
for valor in df.item_price:
    lista.append(float(valor[1:]))
df.item_price = lista 
df["choice_description"] = df["choice_description"].replace(np.NaN, "ninguno")
df["choice_description"] = df["choice_description"].replace("N/A", "NO")
promedio = df.groupby("item_name").agg({"item_price":"mean"}).round(2)
diccionario = promedio.to_dict()

promedio.item_price.to_list()