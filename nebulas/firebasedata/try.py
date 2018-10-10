
list=[["a","b"],["c","d"]]
lista=[]
for i in range(len(list)):
    lista.append("".join(list[i]))
print(lista)
if "a" in lista:
    print("hh")
print("".join(lista))

data = {'add': ['add','919','612']}
if 'add' in data:
    print(data['add'][1])