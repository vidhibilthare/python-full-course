# # def add(a,b):
# #     return a+b
# # print(add(3,4))

# def new_add(*args):
#     total=0
#     for num in args:
#         total+=num
#     return total
# # print(new_add(2,3,4,5))
# l=[2,3,4,5]
# print(new_add(*l))

# kwarg--kyeword argument
def func(**kwargs):
    print(kwargs)
func(name='vidhi',age=30)
# gether as dictionary

# *args,**kwargs,normal parameter,default parameter

# PADK-parameter,args,default,kwargs

def fun2(name,*arg,last_name='unknown',**kwargs):
    print(name)
    print(arg)
    print(last_name)
    print(kwargs)
fun2('vidhi',1,2,3,a=2 ,b=4)