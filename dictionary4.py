# fromkeys , get , clear , copy methods

# fromkeys
# d = {'name':'unknown','age':'unknown'}

# d=dict.fromkeys(['name','hight','age'],'unknown')
# e=dict.fromkeys(('name','hight','age'),'unknown')
# f=dict.fromkeys('abc','unknown')
# g=dict.fromkeys(range(1,11),'unknown')
# print(d)
# print(e)
# print(f)
# print(g)


# get methods
d = {'name':'unknown','age':'unknown'}
# print(d['name'])
print(d.get('names'))

if 'name' in d:
    print('present')
else:
    print('absent')

if d.get('names'):
    print('yes')
else:
    print('no')

# if None --->False else--->True

#clear

# d.clear()
# print(d)

#copy
d1=d.copy()
# d1=d
# print(d1.popitem())
# print(d)
print(d1 is d)