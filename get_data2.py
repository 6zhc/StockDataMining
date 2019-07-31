import requests
import json
from datetime import date, timedelta

yesterday = (date.today() + timedelta(days=-1)).strftime("%Y%m%d")

file_name = "dict.json"
f = open(file_name, "r", encoding="utf-8")
dict_old = json.load(f)
f.close()

k = 0


for item in dict_old:
    response = requests.get("http://q.stock.sohu.com/hisHq?code=cn_"
                            + str(item[0]).zfill(6) + "&start=" + "20190725"
                            + "&end=" + yesterday + "&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp")
    # print(response.url)
    if response.status_code == 200:
        data = (response.text.lstrip("historySearchHandler(["))
        data = data.rstrip("])\n")
        temp = json.loads("{}")
        try:
            for hq in json.loads(data)["hq"]:
                temp.update({hq[0].replace('-', ''): [hq[5], hq[6], float(hq[8])/float(hq[7])*100]})
            file_name = "data/" + str(item[0]).zfill(6) + ".json"
            f = open(file_name, "w", encoding="utf-8")
            json.dump(temp, f, indent=4, ensure_ascii=False)
            f.close()

            file_name = "data_backup/" + str(item[0]).zfill(6) + ".json"
            f = open(file_name, "w", encoding="utf-8")
            json.dump(temp, f, indent=4, ensure_ascii=False)
            f.close()
        except:
            print(response.url)
    k += 1
    print("Finish: " + str(k) + "/ " + str(len(dict_old)))