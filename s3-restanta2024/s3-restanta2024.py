import pandas as pd

df_caen=pd.read_csv("CAEN2_2021_NSAL.csv")
df_populatie=pd.read_csv("PopulatieLocalitati.csv")

#1
df_nou=df_caen.copy()
coloane=df_nou.columns[1:]
df_nou["Total"]=df_nou[coloane].sum(axis=1)
df_nou[coloane]=df_nou[coloane].div(df_nou["Total"], axis=0)
df_nou[coloane]=df_nou[coloane].round(2)
df_nou=df_nou.drop(columns="Total")
df_nou.to_csv("Cerinta1.csv", index=False)

#2
merged=pd.merge(df_caen, df_populatie, left_on="SIRUTA", right_on="Siruta")
pop=merged.groupby("Judet")["Populatie"].sum()
v=merged.groupby("Judet")[coloane].sum()
v_100000=v.div(pop, axis=0)*10000
v_100000=v_100000.round(2).reset_index()
v_100000.to_csv("Cerinta2.csv", index=False)

#3
#--AF FARA ROTATIE
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from factor_analyzer import FactorAnalyzer, calculate_kmo
#INCARCARE STANDARDIZARE DATE
data = pd.read_csv('CAEN2_2021_NSAL.csv', index_col=0)
scaler = StandardScaler()
x = scaler.fit_transform(data)
#TEST KMO
kmo_all, kmo_model = calculate_kmo(x)
print("Indicele KMO global:", round(kmo_model, 4))
print("\nIndicele KMO pe variabile:")
for i, col in enumerate(data.columns):
    print(f"{col}: {round(kmo_all[i], 4)}")
#APLICARE AF FARA ROTATIE
#NR FACTORI: maxim N-1 (criteriul Kaiser)
n_factors = x.shape[1] - 1
efa = FactorAnalyzer(n_factors=n_factors, rotation=None)
scores = efa.fit_transform(x)  #SCORURI FACTORIALE
#SALVARE SCORURI IN CSV
scoruri_df = pd.DataFrame(scores, index=data.index, columns=[f'F{i+1}' for i in range(scores.shape[1])])
scoruri_df.to_csv('f.csv')
print("\nScorurile factoriale au fost salvate în fișierul 'f.csv'.")
#GRAFIC SCORURI PRIMII 2 FACTORI
plt.figure(figsize=(10, 8))
plt.title('Scorurile factoriale pentru primii doi factori')
plt.xlabel('Factorul 1')
plt.ylabel('Factorul 2')
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.scatter(scores[:, 0], scores[:, 1], c='green', s=50)
#ETICHETE
for i, txt in enumerate(data.index):
    plt.annotate(txt, (scores[i, 0], scores[i, 1]), fontsize=8, alpha=0.7)
plt.grid(True)
plt.tight_layout()
plt.show()



