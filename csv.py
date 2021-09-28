import pandas as pd


def casos(ruta_archivo: str)-> dict:
    df = pd.read_csv(ruta_archivo)
    df["Sexo"] = df["Sexo"].replace("f", "F")
    df["Sexo"] = df["Sexo"].replace("m", "M")
    df["Sexo"] = df["Sexo"].replace("M", "M")
    df["Sexo"] = df["Sexo"].replace("F", "F")
    sexo = df.groupby("Sexo").agg({"Edad":"mean"}).round(4)
    dicc_sexo = sexo.to_dict()
    
    dep = df.groupby("Departamento o Distrito").agg({"Edad":"mean"}).round(4)
    dicc_dep = dep.to_dict()
    
    

    lista2 = list()
    for valor in df["Sexo"]:
        lista2.append(valor)
    dip = dict()
    pa = df["Sexo"].value_counts(lista2)*100
    dip = pa.to_dict()
    for i in dip:
        f = dip.get(i)
    for i in dip:
        f = dip.get(i)
        p = round(f, 4)
        dip[i] = p
    
    keyG = sorted(dip)
    
    gen = dict()
    for ca in keyG:
        gen[ca] = dip.get(ca)


    
    #desde acá es el problema con el valor
    lista = list()
    for valor in df["País de procedencia"]:
        lista.append(valor)
    
    paisv = df["País de procedencia"].value_counts(lista)*102.705
    dicpais = paisv.to_dict()

    for i in dicpais:
        f = dicpais.get(i)
    for i in dicpais:
        f = dicpais.get(i)
        p = round(f, 4)
        dicpais[i] = p
    keys = sorted(dicpais)
    
    pais = dict()
    for ca in keys:
        pais[ca] = dicpais.get(ca)
       
    dicDep = dict()   
    dicDep = dicc_dep.get("Edad")

    listaFinal = list()
    listaFinal.append(gen)
    listaFinal.append(dicDep)
    listaFinal.append(pais)
    return listaFinal

casos("D:\Escritorio\Luis\Proyectos\Casos_positivos_de_COVID-19_en_ColombiaDiezMil.csv")
