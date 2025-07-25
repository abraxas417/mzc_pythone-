#dic10.py

dic = {'a': 1, 'b': 2, 'c': 3}

for key in dic.keys():
    print(key, dic[key])



for key in dic:
    print(key, dic[key])

for value in dic.values():
    print(value)

for key, value in dic.items():
    print(key, value)


dic.pop('b')

print(dic)