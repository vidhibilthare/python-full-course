# list comprehension with if statement

number =list(range(1,11))
print(number)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_num =[2,4,6,8]
# num = []
# for i in number:
#     if i%2==0:
#         num.append(i)
# print(num)
even_num = [i for i in number if i%2==0]
print(even_num)
even_num2 = [i for i in range(1,11) if i%2==0]
print(even_num2)
odd_num = [i for i in number if i%2!=0]
print(odd_num)
odd_num2 = [i for i in range(1,11) if i%2!=0]
print(odd_num2)

