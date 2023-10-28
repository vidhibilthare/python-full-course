# function returning function/

# def square(a):
#     return a**2
def  outer_fun():
    def inner_fun():
        print("inside inner func..")
    return inner_fun
# var = outer_fun()
# var()

def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2

var = outer_func2("hello there..!")
var()