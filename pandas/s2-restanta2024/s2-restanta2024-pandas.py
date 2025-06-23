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

#2. coeficienti de variatie fiecare indicator la nivel de continent
#join la cele 2 fisiere pe baza coloanei Cod
join_netflix_coduri=pd.merge(df_netflix, df_coduri, on="Cod")
indicatori=['Librarie','CostLunarBasic','CostLunarStandard','CostLunarPremium','Internet','HDI','Venit','IndiceFericire','IndiceEducatie']
#grupare dupa continent - agg pentru calcul statistici
coef_variatie=join_netflix_coduri.groupby("Continent")[indicatori].agg(['mean', 'std'])
#coef_variatie=abatere std / medie - .xs extrage o sectiune (axis=1-coloane, axis=0-randuri)
coef_variatie=(coef_variatie.xs('std', axis=1, level=1)/coef_variatie.xs('mean', axis=1, level=1)).round(3)
coef_variatie=coef_variatie.reset_index()
coef_variatie=coef_variatie.sort_values(by="Librarie", ascending=False)
coef_variatie.to_csv("Cerinta2.csv", index=False)






