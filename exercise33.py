# make a function 'divide'
# divide (a,b)
# print(divide(4,2)),2
# print(divide(4,0)) ,please don't devide by  zero
# print(divide('4',2)),error
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)   
print(divide(10/'2'))