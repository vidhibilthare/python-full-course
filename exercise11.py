# define a function for greater number

def greater_num(num1,num2):

    if num1>num2:
        return "input 1 is greater number..."
    return "input 2 is greater number..."

print(greater_num(3,4))


num1=int(input("enter a number:-"))
num2=int(input("enter a number:-"))
bigger = greater_num(num1,num2)
print(f"{bigger} is greater")