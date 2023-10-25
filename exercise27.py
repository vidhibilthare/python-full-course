# this is challenge

# define a function take any no of lists containing number
# [1,2,3],[4,5,6],[7,8,9]
# return avarage
# (1+4+7)/3,(2+5+8)/3,(3+6+9)/3
#try to make this anonymous function in one line using lambda

# def avarage_finder(l1,l2):
#     avarage = []
#     for pair in zip(l1,l2):
#         avarage.append(sum(pair)/len(pair))
#     return avarage
# print(avarage_finder([1,2,3],[4,5,6]))

# def avarage_finder(*args):
#     avarage = []
#     for pair in zip(*args):
#         avarage.append(sum(pair)/len(pair))
#     return avarage
# print(avarage_finder([1,2,3],[4,5,6],[7,8,9]))

# args==>tuples


avarage_find=lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(avarage_find([1,2,3],[4,5,6],[7,8,9]))