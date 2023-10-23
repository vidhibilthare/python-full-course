# lambda expression practice
# def is_even(a):
#     if a%2==0: #a%2==0-->True,False
#         return True
#     else:
#         return False
# print(is_even(4))

# is_even2 = lambda a:a%2==0
# print(is_even2(3))

# def last_char(s):
#     return s[-1]
# print(last_char('Vidhi')

# last_char = lambda s:s[-1]
# print(last_char('vidhi'))

# lamba with if , else
# def func(s):
#     if len(s)<5:
#         return True
#     else:
#         return False
# print(func('shukla'))

# func = lambda s : True if len(s) > 5 else False
# print(func('himanshu'))
func = lambda s : len(s)>5
print(func('vidhibilthare'))