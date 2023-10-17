# looping in tuples
# tuple with one elements
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples


mixed=(1,2,3,4,5.1)

# for loop in tuples
for i in mixed:
    print(i)

# you can use while loop too

# tuple with one elements
num =('1',) #(1)->int ('1')-->str
words=('word1','word2')
print(type(num))
print(type(words))
print(type(mixed))

# tuple without parenthesis

car = 'scoripo','kia','indica','yamaha'
print(car)
print(type(car))

# tuple unpacking
car = ('scoripo','kia','indica','yamaha')
car1,car2,car3,car4=(car)
print(car1)
print(car2)
print(car3)
print(car4)

# list inside tuples
fruits = ('mango',['apple','orange'],'banana')
fruits[1].pop()
fruits[1].append("kiwi")
print(fruits)

# some functions that you can use with tuples

# min,max,sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))