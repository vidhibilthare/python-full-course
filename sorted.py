# sorted functions

fruits =['grapes','mango','apple']
fruits.sort()
print(fruits)

# fruits2 = ('grapes','mango','apple')
# sorted(fruits2 )
# print(fruits)

# fruits3 = {'grapes','apple','mango'}
# sorted(fruits3)
# print(fruits)

guitars =[
    {'model':'yamaha','price':84000},
    {'model':'hero','price':94000},
    {'model':'honda','price':80000},
    {'model':'scarpio','price':74000}
]

print(sorted(guitars,key = lambda d:d['price'],reverse=True))