import pandas as pd

df_caen=pd.read_csv("CAEN2_2021_NSAL.csv")
df_populatie=pd.read_csv("PopulatieLocalitati.csv")

#1
df_caen["Total"]= df_caen.iloc[:, 1:].sum(axis=1)
coloane= df_caen.columns[1:-1]
df_caen[coloane]=df_caen[coloane].div(df_caen["Total"], axis=0).round(2)
df_caen=df_caen.drop(columns=["Total"])
df_caen.to_csv("Cerinta1.csv", index=False)

#2
merged=pd.merge(df_caen, df_populatie, left_on="SIRUTA", right_on="Siruta")
coloane= df_caen.columns[1:]
pop=merged.groupby("Judet")["Populatie"].sum()
nr_ang=merged.groupby("Judet")[coloane].sum()
nr_ang= nr_ang.div(pop, axis=0) * 100000
nr_ang=nr_ang.reset_index()
nr_ang.to_csv("Cerinta2.csv", index=False)


