import pandas as pd
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
df_coduri=pd.read_csv("CoduriTari.csv")
df_netflix=pd.read_csv("Netflix.csv")

#1
coloane=["Librarie", "CostLunarBasic", "CostLunarStandard", "CostLunarPremium", "Internet", "HDI", "Venit", "IndiceFericire", "IndiceEducatie"]
standardizat=scaler.fit_transform(df_netflix[coloane])
df_standardizat=pd.DataFrame(standardizat, columns=coloane)
df_standardizat["Cod"]=df_netflix["Cod"]
df_standardizat["Tara"]=df_netflix["Tara"]
df_standardizat=df_standardizat[["Cod", "Tara"] + coloane]
df_standardizat=df_standardizat.sort_values(by="Internet", ascending=False)
df_standardizat.to_csv("Cerinta1.csv", index=False)

#2
merged=pd.merge(df_netflix, df_coduri, on="Cod")
indicatori=['Librarie','CostLunarBasic','CostLunarStandard','CostLunarPremium','Internet','HDI','Venit','IndiceFericire','IndiceEducatie']
grupate=merged.groupby("Continent")[indicatori].agg(['mean', 'std'])
grupate=(grupate.xs('std', axis=1, level=1) / grupate.xs('mean', axis=1, level=1)).round(3).reset_index()
grupate=grupate.sort_values(by="Librarie", ascending=False)
grupate.to_csv("Cerinta2.csv", index=False)






