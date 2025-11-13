import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

API_TOKEN = "79df369c68fa417296dfdb3a5986ef6d" 
TEAM_ID = 64 
DB_URI = "postgresql+psycopg2://postgres:postgres@localhost:5432/football"

def calculate_age(birthdate_str):
    if not birthdate_str:
        return None
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

url = f"https://api.football-data.org/v4/teams/{66}"
headers = {"X-Auth-Token": API_TOKEN}

response = requests.get(url, headers=headers)
data = response.json()

players_list = []

for player in data.get("squad", []):
    players_list.append({
        "id": player.get("id"),
        "name": player.get("name"),
        "position": player.get("position"),
        "nationality": player.get("nationality"),
        "dateOfBirth": player.get("dateOfBirth"),
        "age": calculate_age(player.get("dateOfBirth")),
    })

df_players = pd.DataFrame(players_list)

print(df_players.head(20))
