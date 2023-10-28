#decorator with arguments

from functools import wraps
def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args,**kwargs)
            print('invalid function')
        return wrapper
    return decorator
#only_data_type_allow
def string_join(*args):
    string = ''
    for i in args:
        string+=i
    return string
print(string_join('himanshu','harshit'))