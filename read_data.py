import json
import numpy as np


def read_data(date = "20190729"):
    file_name = "dict.json"
    f = open(file_name, "r", encoding="utf-8")
    dict_old = json.load(f)
    f.close()

    dict_train = dict_old[:int(-len(dict_old)/3)+1]
    dict_test = dict_old[(len(dict_old)-int(len(dict_old)/3)):len(dict_old)]

    data_train_x = []
    data_train_y = []

    for item in dict_train:
        try:
            file_name = "data/" + item[0] + "_" + date + ".json"
            f = open(file_name, "r", encoding="utf-8")
            temp_data = json.load(f)
            temp_x = []
            # 一支股票一天(20190730)的交易记录
            for i in range(242):
                # temp_data[i][0] 某一时刻的时间 我觉得没有用。
                # [temp_data[i][1], temp_data[i][2], temp_data[i][3]] [某一时刻的 最低，最高交易价格，交易量]
                temp_x.append([temp_data[i][1], temp_data[i][2], temp_data[i][3]])
            f.close()

            file_name = "data/" + item[0] + ".json"
            f = open(file_name, "r", encoding="utf-8")
            temp_data = json.load(f)
            # temp_y = [temp_data[date][0], temp_data[date][1]]
            temp_y = temp_data[date][2]
            f.close()

            data_train_x.append(temp_x)
            data_train_y.append(temp_y)
        except Exception as e:
            print('error: ' + item[0] + '_' + date)
            print(e)

    data_train_x = np.array(data_train_x)
    data_train_y = np.array(data_train_y)
    # data_train_y = data_y.reshape(data_y.shape[0],data_train_y.shape[1])
    data_train_y = data_train_y.reshape(data_train_y.shape[0], 1)
    print("train-X 数据格式：" + str(data_train_x.shape))
    print("train-Y 数据格式：" + str(data_train_y.shape))

    data_test_x = []
    data_test_y = []

    for item in dict_test:
        try:
            file_name = "data/" + item[0] + "_" + date + ".json"
            f = open(file_name, "r", encoding="utf-8")
            temp_data = json.load(f)
            temp_x = []
            # 一支股票一天(20190730)的交易记录
            for i in range(242):
                # temp_data[i][0] 某一时刻的时间 我觉得没有用。
                # [temp_data[i][1], temp_data[i][2], temp_data[i][3]] [某一时刻的 最低，最高交易价格，交易量]
                temp_x.append([temp_data[i][1], temp_data[i][2], temp_data[i][3]])
            f.close()

            file_name = "data/" + item[0] + ".json"
            f = open(file_name, "r", encoding="utf-8")
            temp_data = json.load(f)
            # temp_y = [temp_data[date][0], temp_data[date][1]]
            temp_y = temp_data[date][2]
            f.close()

            data_test_x.append(temp_x)
            data_test_y.append(temp_y)
        except Exception as e:
            print('error: ' + item[0] + '_' + date)
            print(e)

    data_test_x = np.array(data_test_x)
    data_test_y = np.array(data_test_y)
    # data_test_y = data_y.reshape(data_y.shape[0],data_test_y.shape[1])
    data_test_y = data_test_y.reshape(data_test_y.shape[0], 1)
    print("test-X 数据格式：" + str(data_test_x.shape))
    print("test-Y 数据格式：" + str(data_test_y.shape))

    return {"input": data_train_x, "output":data_train_y, "input_test": data_test_x, "output_test":data_test_y}


read_data()
