import pandas as pd

df_ensal=pd.read_csv("E_NSAL_2008-2021.csv")
df_populatie_loc=pd.read_csv("PopulatieLocalitati.csv")

#1
ani = df_ensal.columns[1:]
df_ensal["Anul"] = df_ensal[ani].idxmax(axis=1)
rezultat = df_ensal[["SIRUTA", "Anul"]]
rezultat.to_csv("Cerinta1.csv", index=False)

#2
merged = pd.merge(df_ensal, df_populatie_loc, left_on="SIRUTA", right_on="Siruta")
pop=merged.groupby("Judet")["Populatie"].sum()
nr_ang=merged.groupby("Judet")[coloane].sum()
rata_ocupare=nr_ang.div(pop, axis=0)
rata_ocupare["RataMedie"]=rata_ocupare.mean(axis=1)
rata_ocupare=rata_ocupare.round(3).reset_index()
rata_ocupare=rata_ocupare.sort_values(by="RataMedie", ascending=False)
rata_ocupare.to_csv("Cerinta2.csv", index=False)

#3
#--LINIARA DISCRIMINANTA
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import seaborn as sns
#INCARCARE DATE
data = pd.read_csv('Pacienti.csv')
X = data.loc[:, 'L_CORE':'BP_ST']
y = data['DECISION']
#IMPARTIRE IN TRAIN/TEST
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42)
#MODEL LDA
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)
#CALCUL SCORURI DISCRIMINANTE
scores = lda.transform(X_test)
#SALVARE SCORURI
df_scores = pd.DataFrame(scores, columns=[f'D{i+1}' for i in range(scores.shape[1])])
df_scores['DECISION'] = y_test.values
df_scores.to_csv('z.csv', index=False)
print("✔ Scorurile discriminante au fost salvate în fișierul 'z.csv'.")
#GRAFIC SCORURI IN PRIMELE 2 AXE DISCRIMINANTE
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df_scores, x='D1', y='D2', hue='DECISION', palette='Set1')
plt.title('Scoruri LDA în primele două axe')
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.tight_layout()
plt.savefig('lda_scores_plot.png')
plt.show()
#PERFORMANTA MODEL
y_pred = lda.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
df_cm = pd.DataFrame(cm, index=lda.classes_, columns=lda.classes_)
df_cm.to_csv('matc.csv')
print("\n✔ Matricea de confuzie a fost salvată în fișierul 'matc.csv'.")
print("\nMatricea de confuzie:\n", df_cm)
#AFISARE ACURATETE
accuracy = accuracy_score(y_test, y_pred)
print(f"\n✔ Acuratețea modelului: {accuracy:.4f}")
print("\n✔ Indicatori detaliați:\n")
print(classification_report(y_test, y_pred))
#APLICARE PE SET DE PREDICTIE
apply_data = pd.read_csv('Pacienti_apply.csv')
apply_X = apply_data.loc[:, 'L_CORE':'BP_ST']
apply_pred = lda.predict(apply_X)
apply_data['Predictie_DECISION'] = apply_pred
apply_data.to_csv('predictii_aplicare.csv', index=False)
print("✔ Predicțiile pe setul de aplicare au fost salvate în 'predictii_aplicare.csv'.")
