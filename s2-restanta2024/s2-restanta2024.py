import pandas as pd
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
df_coduri=pd.read_csv("CoduriTari.csv")
df_netflix=pd.read_csv("Netflix.csv")

#1
coloane=["Librarie", "CostLunarBasic", "CostLunarStandard", "CostLunarPremium", "Internet", "HDI", "Venit", "IndiceFericire", "IndiceEducatie"]
df_nou=df_netflix.copy()
df_nou[coloane]=scaler.fit_transform(df_nou[coloane])
df_nou=df_nou.sort_values(by="Internet", ascending=False)
df_nou.to_csv("Cerinta1.csv", index=False)

#2
merged=pd.merge(df_netflix, df_coduri, on="Cod")
indicatori=['Librarie','CostLunarBasic','CostLunarStandard','CostLunarPremium','Internet','HDI','Venit','IndiceFericire','IndiceEducatie']
grupate=merged.groupby("Continent")[indicatori].agg(['mean', 'std'])
grupate=(grupate.xs('std', axis=1, level=1) / grupate.xs('mean', axis=1, level=1)).round(3).reset_index()
grupate=grupate.sort_values(by="Librarie", ascending=False)
grupate.to_csv("Cerinta2.csv", index=False)

#3
#--ACP
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
#INCARCARE DATE
data = pd.read_csv('Netflix.csv', index_col=0)
#STANDARDIZARE
scaler = StandardScaler()
x = scaler.fit_transform(data[coloane])
#APLICARE ACP
pca = PCA()
C = pca.fit_transform(x)  #SCORURI
#VARIANTE COMPONENTE PRINCIPALE
alpha = pca.explained_variance_
print("Varianțele componentelor principale (valori proprii):")
for i, val in enumerate(alpha):
    print(f"Componenta {i+1}: {val:.4f}")
#SALVARE SCORURI
scoruri_df = pd.DataFrame(C, index=data.index, columns=[f'C{i+1}' for i in range(C.shape[1])])
scoruri_df.to_csv('scoruri.csv')
print("\nScorurile au fost salvate în fișierul 'scoruri.csv'.")
#GRAFIC SCORURI IN PRIMELE DOUA AXE PRINCIPALE
plt.figure(figsize=(10, 8))
plt.title('Scorurile instanțelor în primele două componente principale')
plt.xlabel('Componenta 1')
plt.ylabel('Componenta 2')
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.scatter(C[:, 0], C[:, 1], c='blue', s=50)
#ADAUGARE ETICHETE
for i, txt in enumerate(data.index):
    plt.annotate(txt, (C[i, 0], C[i, 1]), fontsize=8, alpha=0.7)
plt.grid(True)
plt.tight_layout()
plt.show()







