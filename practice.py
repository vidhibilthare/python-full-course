# fabonacci series

x=0
y=1
z=0
for i in range(1,11):
    print(z)
    x=y
    y=z
    z=x+y


# factorial number
number=int(input("enter number"))
fact=1
if number<0:
    print("no factorial")
elif number == 1 or number == 0:
    print("factorial is 1")
else:
    for i in range(1,number+1):
        fact = fact*i
        number+=1
    print(fact)

#table print

num=3
for i in range(1,11):
    table=i*num
print(table)

# prime number

num=int(input("enter any number:-"))
if num == 0 or num == 1:
    print("not prime number")
if num > 1:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
    else:
        print("prime")

string="vidhi"
c=string.count('i')
print(c)