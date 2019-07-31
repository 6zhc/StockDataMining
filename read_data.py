import json
import numpy as np


def read_data():
    file_name = "dict.json"
    f = open(file_name, "r", encoding="utf-8")
    dict_old = json.load(f)
    f.close()

    data = []

    for item in dict_old:
        file_name = "data/" + item[0] + "_" + "20190730" + ".json"
        f = open(file_name, "r", encoding="utf-8")
        temp_data = json.load(f)
        temp = []
        # 一支股票一天(20190730)的交易记录
        for i in range(242):
            # temp_data[i][0] 某一时刻的时间 我觉得没有用。
            # [temp_data[i][1], temp_data[i][2], temp_data[i][3]] [某一时刻的 最低，最高交易价格，交易量]
            temp.append([temp_data[i][1], temp_data[i][2], temp_data[i][3]])
        data.append(temp)
        f.close()

    data = np.array(data)
    print("数据格式：" + str(data.shape))
    return data


read_data()
