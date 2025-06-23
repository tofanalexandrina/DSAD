import pandas as pd
from sklearn.preprocessing import StandardScaler

df_coduri=pd.read_csv("CoduriTari.csv")
df_netflix=pd.read_csv("Netflix.csv")

#1. standardizare set + descrescator
coloane_pentru_standardizare=["Librarie","CostLunarBasic","CostLunarStandard","CostLunarPremium","Internet","HDI","Venit","IndiceFericire","IndiceEducatie"]
scaler=StandardScaler()
set_standardizat=scaler.fit_transform(df_netflix[coloane_pentru_standardizare])
#construire dataframe
df_set_standardizat=pd.DataFrame(set_standardizat, columns=coloane_pentru_standardizare)
df_set_standardizat["Cod"]=df_netflix["Cod"]
df_set_standardizat["Tara"]=df_netflix["Tara"]
#reordonare coloane
df_set_standardizat=df_set_standardizat[["Cod", "Tara"]+coloane_pentru_standardizare]
df_set_standardizat=df_set_standardizat.sort_values(by="Internet", ascending=False)
df_set_standardizat.to_csv("Cerinta1.csv", index=False)




