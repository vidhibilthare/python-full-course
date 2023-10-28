def decorater_func(any_func):
    def wrapper_func(*args,**kwargs):
        print("this is awesome function..")
        return any_func(*args,**kwargs)
    return wrapper_func

@decorater_func
def func1(a):
    print(f"this is function 1 with argument {a}")

@decorater_func
def add(a,b):
    return a+b
print(add(2,3))


func1(2)