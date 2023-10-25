# advanced min, max functions

# numbers = [1,3,4,8,6]
# print(max(numbers))
# print(min(numbers))
# def func(items):
#     return len(items)
# names = ['himanshu','vidhi','yash','k']
# print(min(names,key = func))


# names = ['vidhi','himanshu','geeta','shivani','satvik']
# print(min(names,key = lambda items : len(items)))

# student2 = [
#     {'name':'vidhi','score':90,'age':20},
#     {'name':'pratima','score':99,'age':24},
#     {'name':'himanshu','score':98,'age':28}
# ]

# print(max(student2,key = lambda item:item.get('age'))['name'])

student1 = {
    'vidhi' : {'score':90,'age':22},
    'pati' : {'score':95,'age':24}
}


print(max(student1,key =lambda item:student1[item]['score']))