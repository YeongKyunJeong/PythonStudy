# dict1.py

# 딕셔너리
# key1 : value1
# key2 : value2

# 변수명 = {key1 : value1, key2 : value2, key3 : value3}

# my_dict = {}
# print(my_dict)
# print(type(my_dict))

# my_dict2 = {0: 1, 1: -2, 2: 3.14}
# print(my_dict2)

my_dict3 = {'이름': '앨리스', '나이': 12, '시력': [1,0, 1.2]}
print(my_dict3)

my_dict3['직업'] = '개발자'
print(my_dict3)
my_dict3['id'] = 'kenneth'
my_dict3['pw'] = 'goodAl35'
print(my_dict3)

print('----------------------')
print(my_dict3['시력'])
print(my_dict3.get('시력'))
print(my_dict3.get('체중'))
print('----------------------')
print(my_dict3.items())
print(type(my_dict3.items()))
print(my_dict3.keys())
print(type(my_dict3.keys()))
print(my_dict3.values)
print('----------------------')

print(type(list(my_dict3.items())[0]))

