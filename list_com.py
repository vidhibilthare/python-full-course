# list comprehension
# with the help of list comprehension we can create of list in one line

# create a  list of square from 1 to 10

# square = []
# for i in range(1,11):
#     square.append(i**2)
# print(square)

# list comprehension

# square = [i**2 for i in range(1,11)]
# print(square)
# negative_list=[]
# for i in range(1,11):
#     negative_list.append(-i)
# print(negative_list)

# negative = [-i for i in range(1,11)]
# print(negative)

names = ['vidhi','himanshu','satvik']
# new_list = ['v','h','s']
# new_list=[]
# for name in names:
#     new_list.append(name[0])
# print(new_list)

list = [name[0] for name in names]
print(list)
