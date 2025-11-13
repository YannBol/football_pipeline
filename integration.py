import pandas as pd
from sqlalchemy import create_engine

csv_file = "joueurs_5_championnats.csv"

df = pd.read_csv(csv_file, header=None, encoding="utf-8-sig")

df.columns = ["team", "player_id", "full_name", "position", "shirt_number", "birth_date", "nationality"]

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/football")

print(f"Nombre de joueurs à insérer : {len(df)}")

df.to_sql("players", engine, if_exists="replace", index=False)

print("✅ Importation réussie")

