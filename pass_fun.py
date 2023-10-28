# pass argument as a functions


# map-->function ko as a argument leta hain
def square(a):
    return a**2
l=[1,2,3,4]
# print(list(map(square,l)))
print(list(map(lambda a:a**2,l)))

def my_map(func,l): 
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list
print(my_map(square,l))
print(my_map(lambda a:a**3,l))

def my_map2(func,l):
    return[func(item) for item in l]
print(my_map2(lambda a:a**3,l))
