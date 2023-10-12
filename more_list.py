# generate list with range function
# something more about pop method
# index method
# pass list to a function

# numbers= list(range(1,11))
# print(numbers)
# pop_item=(numbers.pop())
# print(pop_item)
# print(numbers)
# numbers=[1,2,3,4,5,6,7,8,9,1,10]
# find=(numbers.index(1,3))
# print(find)

numbers=[1,2,3,4,5,6,7,8,9,1,10]
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))