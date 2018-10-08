import json as js
import difflib

f = open('F://test//1.json', encoding='UTF-8')
m = open('F://test//2.json', encoding='UTF-8')

x = js.load(f)
y = js.load(m)

for my_key in x.keys():
    value_eval = x[str(my_key)]
    value_test = y[str(my_key)]
    diff = difflib.SequenceMatcher(None, value_eval, value_test).quick_ratio()
    print(my_key, diff)