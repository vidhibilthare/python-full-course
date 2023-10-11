# fibonacci series

# 0 1 1 2 3 5 8 13 21 34

# user inputs

# 1--->0
# 2--->0,1
# 2--->0,1,2
# 3--->0,1,1,2
# 4-->0,1,1,2,3
# 5-->0,1,1,2,3,5
# 6-->0,1,1,2,3,5,8
# 7-->0,1,1,2,3,5,8,13
# 8-->0,1,1,2,3,5,8,13,21
# 9-->0,1,1,2,3,5,8,13,21,34
# 10-->0,1,1,2,3,5,8,13,21,34,55
# for i in range(1,11):
#  print(i,end=" ")

# def fibonacci_seq(n):
#     a=0 #first number
#     b=1 #second number
#     if n == 1:
#         print(a)
#     elif n==2:
#         print(a,b)
#     else:
#         print(a,b,end=" ")
       
#         for i in range(n-2):
#             c=a+b
#             a=b
#             b=c
#             print(b,end=" ")
    
# fibonacci_seq(10)

x=0
y=1
z=0
for i in range(1,11):
    print(z,end=" ")
    x=y
    y=z
    z=x+y