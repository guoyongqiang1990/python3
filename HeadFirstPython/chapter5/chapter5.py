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

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:    #迭代处理各个列表中的各个数据项
    clean_james.append(sanitize(each_t))
for each_t in julie:
    clean_julie.append(sanitize(each_t))
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))

print(sorted(clean_james, reverse=True))  #sort()和sorted()默认对数据进行升序排序，如果需要降序排序，需要加入reverse = True参数
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))