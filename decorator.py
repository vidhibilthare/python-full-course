# decorator-enhance the functionality of other functions
# @ use for decorator-(syntatic sugur)

def decorator_func(any_func):
    def wrapper_fun():
        print('this is awesome function')
        any_func()
    return wrapper_fun

# this is awesome function
@decorator_func #sortcut
def fun1():
    print('this is function 1')

fun1()
@decorator_func
def fun2():
    print("this is function 2")
fun2()



# # this is awesome function
# def fun2():
#     print("this is function 2")

# # var = decorator_func(fun2)
# # var()
# fun1 =decorator_func(fun1)
# fun1()