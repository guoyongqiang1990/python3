import random
import string

arg1 = "01".join(random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 5)).replace(" ", "")
arg2 = "[" + '"' + arg1 + '"' + ''',"2222"]'''
print(arg2)
print('''["%s","111"]'''%arg1)


print('%s' %'test')
print('%s %s %s' %('test','"aaa"','[]'))