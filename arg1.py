# *args with normal parameter


# def multipy_num(num,*arg):
#     multipy=1
#     print(num)
#     print(arg)
#     for i in arg:
#         multipy*=i
#     return multipy
# print(multipy_num(2,2,3,4))

def multipy_num(num1,num2,*arg):
    multipy=1
    print(num1)
    print(num2)
    print(arg)
    for i in arg:
        multipy*=i
    return multipy
print(multipy_num(2,2,3,4))