# any, all functions
# all function check all the value iterable is True or Falses 
num1 =[2,4,6,8,10,5]
num2 =[1,3,5,6,7,9]

# evens =[]
# for num in num1:
    # evens.append(num%2==0)
# print(evens)

# print(all([True, True, True, True, True]))#-->true

print(all([num%2==0 for num in num1 ]))
print(any([num%2==0 for num in num2 ]))