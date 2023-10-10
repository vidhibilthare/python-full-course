# if elif else statement

#show ticket pricing
# 0 to 3--->free
# 4 to 10--->150
# 11 to 60--->250
# above 60--->200
user_age = input("enter your age:-")
user_age = int(user_age)
if user_age == 0 or user_age <= 3:
    print("free")
elif user_age == 4 or user_age <=10:
    print("150")
elif user_age == 11 or user_age <= 60:
    print("250")
else:
    print("200")
