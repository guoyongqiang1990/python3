# -*- coding: utf-8 -*-
import os, sys
import csv

#读取csv数据

def read_csvdata(csvpath):
    csvdata = []
    try:
        with open(csvpath, 'r') as csvfile:
            reader = csv.reader(csvfile)
            #csvdata = csvfile.read()
            #print(csvdata)

            for line in reader:
                csvdata.append(line)
            print(csvdata)
        return csvdata
    except IOError as err:
        print("File Error: " + str(err))


read_csvdata("data-export.csv")
"""
lista = ["12,345"]
print("".join(lista).split(","))
listb = ["2","3","4"]
#print(listb)
for each in lista:
    each = each.split(",")
    print(each)

for i in range(len(lista)):
    lista[i] = "".join(lista[i]).split(",")
    #print(lista[i].split(','))

print(lista)"""
