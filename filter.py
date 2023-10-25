# filter functions

def is_even(a):
    return a%2==0

numbers = [3,4,2,1,5,6,7,8,9]

# evens = tuple(filter(is_even,numbers))
# evens = tuple(filter(lambda a:a%2==0,numbers))
# print(evens)

evens = tuple(filter(lambda a:a%2==0,numbers))
# for i in evens:
#     print(i)
# for i in evens:
#     print(i)

new_evens = [i for i in numbers if i%2==0]
print(evens)
print(new_evens)



