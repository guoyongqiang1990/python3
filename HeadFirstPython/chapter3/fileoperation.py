#import os
#print(os.getcwd())
import pickle
import standardout
#import sys; sys.path
#打开一段对话，并转存
man = []
other = []

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print('said：', end='')
            print(line_spoken, end='')
            line_spoken = line_spoken.strip()
            if role == "Man":
                man.append(line_spoken)
            elif role == "Other Man":
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print("The data file is missing!")

#输出错误，校验文件
try:
    man_file = open("man_file.txt", "w")
    other_file = open("other_file.txt", "w")
    print(man, file=man_file)
    print(other, file=other_file)

except IOError as err:
    print("File Error: " + str(err))

finally:
    if "man_file" in locals():
        man_file.close()
    if "other_file" in locals():
        other_file.close()

#使用with，不使用 finall
try:
    with open("man_file.txt", "w") as man_file2:
        standardout.print_lol(man, True, 0, man_file2)
#        print(man, file=man_file2)
    with open("other_file.txt", "w") as other_file2:
        standardout.print_lol(other, True, 0, other_file2)

except IOError as err2:
    print("File Error: " + str(err2))

#腌制man_file和other_file的数据
try:
    with open('man_data.txt', 'wb')as man_file, open('other_data.txt', 'wb')as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print("File Error: " + str(err))
except pickle.PickleError as perr:
    print("Pickling error: " + str(perr))

out = open("data.out", "w")
print("Norwegian Blues stun easily.", file=out)
out.close()