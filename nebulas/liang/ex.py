str1 = 'lucky'

var1 = 'nas nano 测试小分队'

print(var1.replace("n", "N"))

print(var1.replace(" ",""))

var2 = "我就是我, \n 就是我"
print(var2)
count = 0

def method():
    global count
    count +=1
    print(count)

method()
print(count)

list = ["a","b","c"]
list.append('d')
list.insert(1,"a")
print(list)

list.remove("c")

print(list)

del list[1]

print(list)

print("".join(list))
print(type("".join(list)))