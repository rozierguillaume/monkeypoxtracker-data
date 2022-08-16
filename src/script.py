import pandas as pd
import json

df = pd.read_csv("https://raw.githubusercontent.com/owid/monkeypox/main/owid-monkeypox-data.csv")
df_world = df[df["location"] == "World"]
df = df[df["location"] != "World"]

df_date_max = df[["location", "date", "total_cases"]].groupby(["location"]).last().reset_index().sort_values(by="total_cases", ascending=False)
df_france = df[["location", "date", "total_cases", "new_cases_smoothed", "new_cases"]][df["location"] == "France"].reset_index()

json_string = {}
json_string["dates"] = df_france.date.tolist()
json_string["total_confirmed_by_entry"] = df_france["total_cases"].fillna(0).tolist()
json_string["new_cases_smoothed"] = df_france["new_cases_smoothed"].fillna(0).tolist()
json_string["new_cases"] = df_france["new_cases"].fillna(0).tolist()

with open('data/monkeypox-france.json', 'w') as outfile:
    json.dump(json_string, outfile)


json_string = {}
json_string["dates"] = df_world.date.tolist()
json_string["total_confirmed_by_entry"] = df_world["total_cases"].fillna(0).tolist()
json_string["new_cases_smoothed"] = df_world["new_cases_smoothed"].fillna(0).tolist()

with open('data/monkeypox-world-only.json', 'w') as outfile:
    json.dump(json_string, outfile)


json_string = {}
json_string["locations"] = df_date_max.location.tolist()
json_string["total_confirmed_by_entry"] = df_date_max["total_cases"].fillna(0).tolist()

with open('data/monkeypox-world-countries-lastdate.json', 'w') as outfile:
    json.dump(json_string, outfile)