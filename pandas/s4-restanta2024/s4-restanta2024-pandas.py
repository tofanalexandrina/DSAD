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
ani = [str(an) for an in range(2008, 2022)]
ang_judet = merged.groupby("Judet")[ani].sum()
pop_judet = merged.groupby("Judet")["Populatie"].sum()
rata_ocupare = ang_judet.div(pop_judet, axis=0).round(3)
rata_ocupare["RataMedie"] = rata_ocupare.mean(axis=1).round(3)
rata_ocupare = rata_ocupare.sort_values(by="RataMedie", ascending=False)
rata_ocupare=rata_ocupare.reset_index()
rata_ocupare.to_csv("Cerinta2.csv", index=False)