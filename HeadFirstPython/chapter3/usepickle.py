import pickle
import standardout

#pickle的使用
with open('mydata.pickle', 'wb') as mysavedata:
    pickle.dump([1,2,"there"], mysavedata)

with open('mydata.pickle', 'rb') as myrestoredata:
    a_list = pickle.load(myrestoredata)

print(a_list)



#腌制后数据的使用
new_man = []
try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File Error: ' + str(err))
except pickle.PickleError as perr:
    print("File Error: " + str(perr))
standardout.print_lol(new_man)
print("\n")
print( new_man[0])
print(new_man[-1])