# -*- coding: utf-8 -*-
import os

def print_dirctory_contents(sPath):
    """
    这个函数接收文件夹的名称作为输入参数
    返回该文件夹中文件的路径
    以及其包含文件夹中文件的路径
    
    """
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_dirctory_contents(sChildPath)
        else:
            print(sChildPath)


if __name__ == "__main__":
    print_dirctory_contents("E:\郭永强\Music\Maroon 5")