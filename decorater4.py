from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wrapper_func(*args,**kwargs):
        print(f"you are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper_func



@print_function_data

def addition(a,b):
    '''this is function takes two numbers as arguments and return their sum'''
    return a+b

print(addition(3,4))

#output
#you are calling add function
#this function take two numbers as parameters and return their sum
#7
