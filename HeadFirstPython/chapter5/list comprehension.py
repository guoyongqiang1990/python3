with open("james.txt") as jaf:
    james = jaf.readline().strip().split(',')

with open("julie.txt") as juf:
    julie = juf.readline().strip().split(',')

with open('mikey.txt') as mif:
    mikey = mif.readline().strip().split(',')

with open('sarah.txt') as saf:
    sarah = saf.readline().strip().split(',')

print(james)
print(julie)
print(mikey)
print(sarah)
print("\n")
print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))
print('\n')

def sanitize(time_string):   #创建函数，转换数据格式
    if '-' in time_string:
        splitter = '-'
        #(mins, secs) = time_string.split(splitter)
    elif ":" in time_string:
        splitter = ':'
        #(mins, secs) = time_string.split(splitter)
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

clean_james = sorted([sanitize(each_t) for each_t in james], reverse=True)       #列表推导代替列表迭代  list comprehension
clean_julie = sorted([sanitize(each_t) for each_t in julie])                     #sort()和sorted()默认对数据进行升序排序，如果需要降序排序，需要加入reverse = True参数
clean_mikey = sorted([sanitize(each_t) for each_t in mikey])
clean_sarah = sorted([sanitize(each_t) for each_t in sarah])

print(clean_james)
print(clean_julie)
print(clean_mikey)
print(clean_sarah)


unique_james = []
unique_julie = []
unique_mikey = []
unique_sarah = []

for each_t in clean_james:                            #取各人成绩前三，并去重
    if each_t not in unique_james:
        unique_james.append(each_t)

for each_t in clean_julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)

for each_t in clean_mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)

for each_t in clean_sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)


print(unique_james[0:3])
print(unique_julie[0:3])
print(unique_mikey[0:3])
print(unique_sarah[0:3])

#用集合删除重复项：用set（）bif创建一个新的空集合，并赋值给一个变量
distances = {10.6, 11, 8, 10.6, "two", 7}  #重复值被自动忽略
james_time = set(james)   #重复值被自动忽略

print(distances)
print(james_time)


print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
