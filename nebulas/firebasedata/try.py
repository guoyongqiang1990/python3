# -*- coding: utf-8 -*-
import os, sys
import csv
import openpyxl
import xlwt

#work to do:干掉converse一列，对比key值

#读取需求excel文档
def read_requirement(requirementpath):
    try:
        with open(requirementpath, 'rb') as requirementfile:
            workbook = openpyxl.load_workbook(requirementfile)
            worksheet = workbook.active
            #print(worksheet.title)
            #将excel数据按行读取成列表
            requirementdata = []
            for i in range(len(list(worksheet.rows))):
                rowdata = []
                for cell in list(worksheet.rows)[i]:
                    rowdata.append(cell.value)
                if type(rowdata[0]) is float: #将不是埋点事件的行去掉
                    requirementdata.append(rowdata)
        return requirementdata
    except IOError as err:
        print("File Error: " + str(err))

print(read_requirement('2.2埋点需求.xlsx'))
