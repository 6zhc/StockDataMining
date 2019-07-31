import requests
import json
from datetime import date, timedelta

yesterday = (date.today() + timedelta(days=-1)).strftime("%Y%m%d")

k = 0
dict = []

file_name = "dict.json"
f = open(file_name, "r", encoding="utf-8")
dict_old = json.load(f)
f.close()

for item in dict_old:
    response = requests.get("http://img1.money.126.net/data/hs/time/4days/0" + str(item[0]).zfill(6) + ".json")
    if response.status_code == 200 and response.json()["data"][0]["date"] == yesterday:
        temp = [str(response.json()["symbol"]), response.json()["name"]]
        dict.append(temp)
        data = response.json()["data"]
        for i in range(0, 4):
            file_name = "data/" + response.json()["symbol"] + "_" + data[i]["date"] + ".json"
            f = open(file_name, "w", encoding="utf-8")
            json.dump(data[i]["data"], f, indent=4, ensure_ascii=False)
            f.close()

            # back up
            file_name = "data_backup/" + data[i]["date"] + "_" + response.json()["symbol"] + ".json"
            f = open(file_name, "w", encoding="utf-8")
            json.dump(data[i]["data"], f, indent=4, ensure_ascii=False)
            f.close()
    k += 1
    print("Finish: " + str(k) + "/ " + str(len(dict_old)))

file_name = "dict.json"
f = open(file_name, "w", encoding="utf-8")
json.dump(dict, f, indent=4, ensure_ascii=False)
f.close()

file_name = "data/dict.json"
f = open(file_name, "w", encoding="utf-8")
json.dump(dict, f, indent=4, ensure_ascii=False)
f.close()

file_name = "data_backup/dict.json"
f = open(file_name, "w", encoding="utf-8")
json.dump(dict, f, indent=4, ensure_ascii=False)
f.close()
