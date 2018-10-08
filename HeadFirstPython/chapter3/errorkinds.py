#输出具体错误
try:
    data = open('missing.txt')
    print(data.readline(),end='')

except IOError as err:
    print("File Error:" + str(err))

finally:
    if 'Data' in locals():
        data.close()

#用finally保证文件关闭
try:
    data1 = open("its.txt", "w")
    print("It's ...", file=data1)

except IOError as err1:
    print("File Error:" + str(err1))

finally:
    if 'data1' in locals():
        data1.close()

#用with保证文件关闭，不需要finally
try:
    with open("its2.txt", "w") as data2:
        print("It's...", file=data2)

except IOError as err2:
    print("FileError" + str(err2))