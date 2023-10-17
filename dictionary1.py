# looping and in keyword

user_info={
    'name': "vidhi",
    'age' : 24,
    'color' : ['black','white'],
    'flower' : ['rose','lotues'],
}

# check if key exits in dictionary
if 'names' in user_info:
    print('present')
else:
    print('no present')

# check if value exits in dictionary
if 24 in user_info.values():
    print('present')
else:
    print('no present')

# loops in dictionaries

# for i in user_info.values():
for i in user_info:
    print(i)#print keys
    print(i)#print value using value method

# list shown and dict type
# values methods
user_info_value=user_info.values()
print(type(user_info_value))

# keys methods
user_info_key=user_info.keys()
print(user_info_key)
print(type(user_info_key))

# loop in dictionary
for i in user_info:
    print(user_info[i])


# items methods
# user_items=user_info.items()
# print(user_items)
# print(type(user_items))

# for looping items method

for key,value in user_info.items():
    print(f"key is {key} and value is {value}")

for i in user_info.items():
    print(i)