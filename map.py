# MAP FUNCTION

numbers =[1,2,3,4]
def squares(a):
    return a**2 

# squares = list(map(squares,numbers))
# # print(squares)

# squares = list(map(lambda a:a**2,numbers))
# print(squares)

# list comprehension
# square_new =[i**2 for i in numbers]
# print(square_new)

# new_list = []
# for num in numbers:
#     new_list.append(squares(num))
# print(new_list)

name =  ['vidhi','irresponsibile','selfish']
length =list(map(len,name))
print(length)