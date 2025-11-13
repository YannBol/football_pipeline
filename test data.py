import pandas as pd
from sqlalchemy import create_engine

csv_file = "C:/Users/yannb/OneDrive/Documents/5_Codage/Projet/data/matchs_ligues.csv"

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/football")

df = pd.read_csv(
    csv_file,
    encoding="utf-8-sig",
    usecols=range(131),
    skiprows=1 

df.columns = df.columns.str.strip()

df.to_sql("matches", engine, if_exists="replace", index=False)

print("✅ Importation réussie : le fichier entier est dans la table 'matches'")

