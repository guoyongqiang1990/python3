# -*- coding: utf-8 -*-
import os, sys
import csv

#读取csv数据

def read_csvdata(csvpath):
    try:
        with open(csvpath, 'r') as csvfile:
            csvdata = csvfile.read()
            print(csvdata)
        return csvdata
    except IOError as err:
        print("File Error: " + str(err))

#处理数据
def data_analysis(csvdata):
    csvdata2 = []
    csvdata = csvdata.split("\n")
    for eachline in csvdata:
        csvdata2.append(eachline.strip().split(','))
    csvdata2 = csvdata2[:-1]
    print(csvdata2)
    # 增加一列
    csvdata2[3].append("result")

    for i in range(4, len(csvdata2)):
        if csvdata2[i][1] == "0" or csvdata2[i][2] == "0":
            csvdata2[i].append('Fail')
        else:
            csvdata2[i].append("Pass")
        print(csvdata2[i])
    return csvdata2

#写数据
def write_csvresult(csvdata):
    csvresult = 'csvtestresult.csv'
    with open(csvresult, 'w') as csvfile2:
        writer = csv.writer(csvfile2)
        for eachline in csvdata:
            writer.writerow(eachline)


if __name__ == "__main__":
    from sys import argv
    #filepath = argv[1]
    filepath = "data-export.csv"
    data = read_csvdata(filepath)
    data2 = data_analysis(data)
    write_csvresult(data2)