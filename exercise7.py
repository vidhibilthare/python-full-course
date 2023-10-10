# problem
# ask user to input a number containing more then one digit
# example - 1256
# calculate 1+2+5+6 and print

# algorithm - (method  to solve  problem in human language)
# ask input in string,i.e don't change string to int
# example - "1256"
#pick string charecter one by one and change to int
#int(example[0])+(example[1])...go upto len(example)

number = input("enter a number form user:-")
# "1234" length=4 last_index=3
# int(number[i])

sum = 0
i=0
while i < len(number):
    sum += int(number[i])
    i+=1
print(sum)