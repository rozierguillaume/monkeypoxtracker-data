import pandas as pd
import json

df = pd.read_csv("https://raw.githubusercontent.com/owid/notebooks/main/EdouardMathieu/monkeypox/owid-monkeypox-data.csv")
df_world = df[df["location"] == "World"]
df = df[df["location"] != "World"]

df_date_max = df[["location", "date", "total_confirmed_by_confirmation"]].groupby(["location"]).last().reset_index().sort_values(by="total_confirmed_by_confirmation", ascending=False)
df_france = df[["location", "date", "total_confirmed_by_confirmation", "7day_confirmed_by_confirmation", "daily_confirmed_by_confirmation"]][df["location"] == "France"].reset_index()

json_string = {}
json_string["dates"] = df_france.date.tolist()
json_string["total_confirmed_by_entry"] = df_france["total_confirmed_by_confirmation"].fillna(0).tolist()
json_string["7day_confirmed_by_confirmation"] = df_france["7day_confirmed_by_confirmation"].fillna(0).tolist()
json_string["daily_confirmed_by_confirmation"] = df_france["daily_confirmed_by_confirmation"].fillna(0).tolist()

with open('data/monkeypox-france.json', 'w') as outfile:
    json.dump(json_string, outfile)


json_string = {}
json_string["dates"] = df_world.date.tolist()
json_string["total_confirmed_by_entry"] = df_world["total_confirmed_by_confirmation"].fillna(0).tolist()
json_string["7day_confirmed_by_confirmation"] = df_world["7day_confirmed_by_confirmation"].fillna(0).tolist()

with open('data/monkeypox-world-only.json', 'w') as outfile:
    json.dump(json_string, outfile)


json_string = {}
json_string["locations"] = df_date_max.location.tolist()
json_string["total_confirmed_by_entry"] = df_date_max["total_confirmed_by_confirmation"].fillna(0).tolist()

with open('data/monkeypox-world-countries-lastdate.json', 'w') as outfile:
    json.dump(json_string, outfile)