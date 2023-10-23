# functions with all parameters
# very important to understand

#PADK
# parameters
# default parameters
#kwargs

# def func(name='unknown',age='unknown'):
#     print(name)
#     print(age)
# func('vidhi')

def func(name,*args,last_name = 'unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('vidhi',2,3,a=2,b=4)

def func2(name,last_name='unknown'):
    print(name)
    print(last_name)
func2('vidhi')