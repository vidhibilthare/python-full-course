# iterator vs iterable

numbers =[1,2,3,4] #,tuple,string---iteranles
squares =map(lambda a:a**2,numbers) #iterator

# for i in numbers:
#     print(numbers)

# numbers_iter = iter(numbers)
# print(next(numbers_iter))
# print(next(numbers_iter))
# print(next(numbers_iter))
# print(next(numbers_iter))

print(iter(numbers)) #list iterator object

