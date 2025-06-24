
import pandas as pd

df_vot=pd.read_csv("Vot.csv")
df_coduri=pd.read_csv("Coduri_localitati.csv")

#1
coloane=["Barbati_25-34","Barbati_35-44","Barbati_45-64","Barbati_65_","Femei_18-24","Femei_35-44","Femei_45-64","Femei_65_"]
df_nou=df_vot.copy()
df_nou[coloane]=df_nou[coloane].div(df_nou["Votanti_LP"], axis=0) *100
final=df_nou.drop(columns="Votanti_LP")
final.to_csv("Cerinta1.csv", index=False)

#2
merged=pd.merge(df_vot, df_coduri, on="Siruta")
grupate=merged.groupby("Judet")[["Barbati_25-34","Barbati_35-44","Barbati_45-64","Barbati_65_","Femei_18-24","Femei_35-44","Femei_45-64","Femei_65_", "Votanti_LP"]].sum().reset_index()
grupate[coloane]=grupate[coloane].div(grupate["Votanti_LP"], axis=0)*100
valori=grupate.drop(columns="Votanti_LP")
valori.to_csv("Cerinta2.csv", index=False)


#3
# ---CANONICA CCA
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cross_decomposition import CCA
import matplotlib.pyplot as plt
#CITIRE
data = pd.read_csv('Vot.csv')
#SEPARARE VARIABILE
set1 = data[[col for col in data.columns if col.startswith("Barbati")]]
set2 = data[[col for col in data.columns if col.startswith("Femei")]]
#STANDARDIZARE
scaler_x = StandardScaler()
scaler_y = StandardScaler()
x = scaler_x.fit_transform(set1)
y = scaler_y.fit_transform(set2)
#NR COMP CANONICE(minim între nr. variabile set1 și set2)
p = x.shape[1]
q = y.shape[1]
m = min(p, q)
#CCA
cca = CCA(n_components=m)
z, u = cca.fit_transform(x, y)  # scoruri canonice
#SALVARE SCORURI
pd.DataFrame(z, columns=[f'z{i+1}' for i in range(m)]).to_csv('z.csv', index=False)
pd.DataFrame(u, columns=[f'u{i+1}' for i in range(m)]).to_csv('u.csv', index=False)
print("Scorurile canonice au fost salvate în 'z.csv' și 'u.csv'.")
#CALCUL CORELATII(RADACINI) CANONICE
r = []
for i in range(m):
    r.append(np.corrcoef(z[:, i], u[:, i])[0, 1])
#SALVARE CORELATII CANONICE
pd.DataFrame({'Corelatie_canonica': r}, index=[f'RC{i+1}' for i in range(m)]).to_csv('r.csv')
print("Corelațiile canonice au fost salvate în 'r.csv'.")
#PLOT SCORURI PENTRU PRIMELE 2 COMP CANONICE
plt.figure(figsize=(8, 8))
plt.title('Biplot - Scoruri canonice (z1,z2) și (u1,u2)')
plt.scatter(z[:, 0], z[:, 1], c='red', label='Z (barbati)')
plt.scatter(u[:, 0], u[:, 1], c='blue', label='U (femei)')
plt.xlabel('Componenta 1')
plt.ylabel('Componenta 2')
plt.legend()
plt.grid(True)
plt.show()
print("Plotul scorurilor canonice a fost generat.")
