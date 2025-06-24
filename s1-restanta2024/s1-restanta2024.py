import pandas as pd
from matplotlib.pyplot import scatter

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

#3
#--CLUSTER
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
#INCARCARE DATE
# Asumăm că prima coloană este indexul
data = pd.read_csv('LocationQ.csv', index_col=0)
#STANDARDIZARE
scaler = StandardScaler()
x = scaler.fit_transform(data)
#ANALIZA IERARHICA METODA WARD
HC = linkage(x, method='ward')
#MATRICE DE JONCTIUNI
print("Matrice ierarhică (linkage matrix):")
print("Cluster1\tCluster2\tDistanță\tNr. instanțe în cluster nou")
for i, row in enumerate(HC):
    print(f"{int(row[0])}\t\t{int(row[1])}\t\t{row[2]:.4f}\t\t{int(row[3])}")
#DETERMINARE PRAG OPTIM
def threshold(h: np.ndarray):
    n = h.shape[0]
    dist_1 = h[1:n, 2]
    dist_2 = h[0:n - 1, 2]
    diff = dist_1 - dist_2
    j = np.argmax(diff)
    t = (h[j, 2] + h[j + 1, 2]) / 2
    return t, j, n
#DETERMINARE NR OPTIM CLUSTERE
t, j, n = threshold(HC)
k = n - j
print(f"\nNumăr de clustere determinat automat: {k}")
print(f"Pragul de tăiere (threshold): {t:.4f}")
#DENDROGRAMA
plt.figure(figsize=(15, 8))
plt.title('Dendrogramă - Metoda Ward')
dendrogram(HC, labels=data.index.tolist(), leaf_rotation=90)
plt.axhline(y=t, c='r', linestyle='--', label=f'Threshold = {t:.2f}')
plt.legend()
plt.tight_layout()
plt.savefig('dendrograma.png')  # Salvează imaginea
plt.show()
#COMPONENTA PARTITIE OPTIMALA
cluster_labels = fcluster(HC, k, criterion='maxclust')
#SALVARE CSV
popt = pd.DataFrame({
    'Judet': data.index,
    'Cluster': cluster_labels
})
popt.to_csv('popt.csv', index=False)
print("\nPartiția optimală a fost salvată în fișierul 'popt.csv'.")








