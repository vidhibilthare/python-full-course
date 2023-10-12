# min and max function in lists

number=[1,5,2]
# print(min(number))
# print(max(number))
def greatest_diff(l):
    return max(l)-min(l)
print(greatest_diff(number))