def add(a,b):
    if (type(a) is int ) and (type(b) is int):
        return a+b
    raise TypeError("oops you are passing wrong datatype to function") 
print(add('3','4'))