#import os
#print(os.getcwd())
#import pickle
#import standardout
#import sys; sys.path
#打开一段对话，并转存
success_num = 0
fail_num = 0

try:
    data = open('log.txt')
    for each_line in data:
        try:
            [log, status] = each_line.split(',', 1)
            print(log, end='')
            print('said：', end='')
            print(status, end='')
            status = status.strip()
            if status == "success":
                success_num += 1
            elif status == "fail":
                fail_num += 1
        except ValueError:
            pass
    print(success_num)
    print(fail_num)
    data.close()

except IOError:
    print("The Data file is missing!")