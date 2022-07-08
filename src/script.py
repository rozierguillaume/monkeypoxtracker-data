import pandas as pd
import json

df = pd.read_csv("https://raw.githubusercontent.com/owid/notebooks/main/EdouardMathieu/monkeypox/owid-monkeypox-data.csv")
df = df[df["location"] != "World"]
df_date_max = df[["location", "date", "total_confirmed_by_confirmation"]].groupby(["location"]).last().reset_index().sort_values(by="total_confirmed_by_confirmation", ascending=False)
df_france = df[["location", "date", "total_confirmed_by_confirmation"]][df["location"] == "France"].reset_index()
json_string = {}
json_string["dates"] = df_france.date.tolist()
json_string["total_confirmed_by_entry"] = df_france["total_confirmed_by_confirmation"].fillna(0).tolist()

with open('data/monkeypox-france.json', 'w') as outfile:
    json.dump(json_string, outfile)


json_string = {}
json_string["locations"] = df_date_max.location.tolist()
json_string["total_confirmed_by_entry"] = df_date_max["total_confirmed_by_confirmation"].fillna(0).tolist()

with open('data/monkeypox-world-lastdate.json', 'w') as outfile:
    json.dump(json_string, outfile)