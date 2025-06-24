import pandas as pd

df_indicatori=pd.read_csv("Indicatori.csv")
df_populatie=pd.read_csv("PopulatieLocalitati.csv")

#1
medie=df_indicatori["CFA"].mean()
localitati=df_indicatori[df_indicatori["CFA"] > medie]
localitati=localitati.sort_values(by="CFA", ascending=False)
localitati.to_csv("Cerinta1.csv", index=False)

#2
merged=pd.merge(df_indicatori, df_populatie, left_on="SIRUTA", right_on="Siruta")
indicatori=["NR_FIRME", "NSAL", "CFA", "PROFITN", "PIERDEREN", "Populatie"]
grupate=merged.groupby("Judet")[indicatori].sum().reset_index()
for coloana in ["NR_FIRME", "NSAL", "CFA", "PROFITN", "PIERDEREN"]:
    grupate[coloana]= grupate[coloana] * 1000 / grupate["Populatie"]
valori=grupate.drop(columns=["Populatie"])
valori.to_csv("Cerinta2.csv", index=False)

