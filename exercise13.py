# define a function which will take list cointaing numbers as a input 
# and return list containing square of every elements
# example
# numbers = [1,2,3,4]
# square_list(numbers)--->return-->[1,4,9,16]

def square_l(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square
numbers=[1,2,3,4]
print(square_l(numbers))
