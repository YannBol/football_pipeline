import pandas as pd
import glob

chemin_dossier = r"C:/Users/yannb/OneDrive/Documents/5_Codage/Projet/data/matches/*.csv"

fichiers = glob.glob(chemin_dossier)

dfs = []

for fichier in fichiers:
    competition = fichier.split("\\")[-1].replace(".csv", "")
    
    df = pd.read_csv(fichier, skiprows=1, encoding="utf-8-sig")
        
    dfs.append(df)

df_final = pd.concat(dfs, ignore_index=True)

print(df_final.head())

df_final.to_csv(r"C:/Users/yannb/OneDrive/Documents/5_Codage/Projet/data/matches_combined.csv", index=False, encoding="utf-8")

