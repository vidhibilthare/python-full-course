#summary dict
#what is dictionary
#unordered collection of data

d = {'name':'vidhi','age':26}


#or
d1=dict(name='vidhi',age=26)

#or
d2 = {
    'name':'vidhi',
    'age':26,
    'colors':['red','yellow','green']
}

#how to access data from dictionary
#you can not do like
#d[0] , necause there is no order inside dictionary

#syntex
#print(dictname[keyname])
# print(d['name'])

# add data inside empty dict
empty_dict = {}
empty_dict['key1']='value1'
empty_dict['key2']='value2'
# print(empty_dict)

# check exitence of value inside dict
# use in keyword to check for keys

# if 'name' in d:
    # print('yes')
# else:
    # print('no')

# how to iterate over dictionary
# most common method
# for key , value in d.items():
    # print(f"key is {key} and value is {value}")

# to print all keys
# for i in d:
#     print(i)

# to print all values
# for i in d.values():
#     print(i)

#most common dict method

# get methods
# to access a key and check existence
# print(d.get('name'))

# why we use get
# to get rid of error
# example
# print(d['name'])
# print(d.get('name'))


# to delete items
# pop--->to take one item 