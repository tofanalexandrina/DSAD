import pandas as pd

df_caen2=pd.read_csv("CAEN2_2021_NSAL.csv")
df_populatie=pd.read_csv("PopulatieLocalitati.csv")

#1. procente angajati pe fiecare ramura per localitate
#calcul total angajati in localitate - toate randurile, coloanele-fara prima
#sum axis=1 ->suma pe randuri
df_caen2["Total"]=df_caen2.iloc[:, 1:].sum(axis=1)
coloane_pentru_procente=df_caen2.columns[1:-1] #fara siruta(prima) si total(ultima)
#calcul procentual
df_caen2[coloane_pentru_procente]=df_caen2[coloane_pentru_procente].div(df_caen2["Total"], axis=0).round(2)
df_caen2=df_caen2.drop(columns=["Total"])
df_caen2.to_csv("Cerinta1.csv", index=False)