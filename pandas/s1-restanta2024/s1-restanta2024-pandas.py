import pandas as pd

df_indicatori=pd.read_csv("Indicatori.csv")
df_populatie=pd.read_csv("PopulatieLocalitati.csv")
df_location=pd.read_csv("LocationQ.csv")

#1. cifra de afaceri (CFA) mai mare decat valoarea medie pe tara + salvare csv + ordine descrescatoare
#media pe tara
media_tara=df_indicatori["CFA"].mean()
#localitati selectare cu cfa > media
localitati_cfa_mai_mare=df_indicatori[df_indicatori["CFA"]>media_tara]
#sortare descrescator
localitati_cfa_mai_mare=localitati_cfa_mai_mare.sort_values(by="CFA", ascending=False)
#salvare csv
localitati_cfa_mai_mare.to_csv("Cerinta1.csv", index=False)

#2. valori indicatori raportate la populatie + la nivel de judet
#fuzionare 2 fisiere necesare (valori indicatori din indicatori.csv si populatie din populatielocalitati.csv)
# dupa coloana comuna
df_fuzionare_fisiere=pd.merge(df_indicatori, df_populatie, left_on="SIRUTA", right_on="Siruta")
#grupare dupa judet dupa fuzionare si alegere coloane de care avem nevoie pentru calcule
# (toate din indicatori.csv si doar populatie din populatielocalitati.csv) ([[]] pt mai multe coloane, [""] pt una)
df_grupare_judet=df_fuzionare_fisiere.groupby("Judet")[["NR_FIRME", "NSAL", "CFA", "PROFITN", "PIERDEREN", "Populatie"]].sum().reset_index()
#calcul conform formulei
for coloana in ["NR_FIRME", "NSAL", "CFA", "PROFITN", "PIERDEREN"]:
    df_grupare_judet[coloana]=df_grupare_judet[coloana]*1000/df_grupare_judet["Populatie"]
#eliminam coloana populatie
valori_indicatori=df_grupare_judet.drop(columns=["Populatie"])
valori_indicatori.to_csv("Cerinta2.csv", index=False)

