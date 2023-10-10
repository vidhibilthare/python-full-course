user_name = input("enter user name:-")
user_age = input("enter user age:-")
user_age = int(user_age)
if user_age > 10 and (user_name[0] == "a" or user_name[0] == "A"):
    print("you can watch movie")
else:
    print("you cant watch movie")
