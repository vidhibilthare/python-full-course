# 3 numbers input from user and find avarage and print with string formatting
# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# num3=int(input("enter third number"))
# sum=num1+num2+num3
# print("sum of numbers is:-",sum)
# avg=sum/3
# print("avg {} sum {}".format(avg,sum))
# print(f"avg {avg} sum {sum}")

# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# num3=int(input("enter third number"))
# print(f"avarage of three numbers{(int(num1)+int(num2)+int(num3))/3}")

num1,num2,num3=input("enter three number seprated by commas").split(",")
print(f"avarage of three numbers{(int(num1)+int(num2)+int(num3))/3}")

