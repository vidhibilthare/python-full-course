# function returning two values-->return tuple

def fun(int1,int2):
    add=int1+int2
    multiple=int1*int2
    return add,multiple

# print(fun(3,4))
add , multiple =fun(3,4)
print(add)
print(multiple)