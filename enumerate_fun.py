# we use enumarate function with for loop track position 
# of our item in iterable 

# how can we do this without enumerate functions
names = ['vidhi','yash','shubhi']
pos = 0
# for name in names:
#     print(f"{pos}----{name}")
#     pos += 1

# with enumerates
# for pos ,name in enumerate(names):
#     print(f"{pos}----{name}")

# define a function that take two arguments
# 1.list containing string
# 2.staring that want to find in your list
# and this function will return the index of string 
# in your list and  if string is not present then return  -1


def find_pos(l,target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
    return -1
print(find_pos(names,'shubhiaa'))

