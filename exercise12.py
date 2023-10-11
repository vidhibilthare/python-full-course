# pallindrome number

# define a pallindrome function that take one word in string as input 
# and return True if it is pallindrome else return False
 

# pallindrome- word that reads same backwords as forwards

# example->
# is_pallindrome("madam")=True
# is_pallindrome("naman")=True
# is_pallindrome("vidhi")=False

# logic algorithm
# step-1
# reverse the string
# compare reverse string with original string

# def is_pallindrome(word):
#     reversed_word=word[::-1]
#     if word == reversed_word:
#         return True
#     return False
# print(is_pallindrome("naman"))
# print(is_pallindrome("121"))

# def is_pallindrome(word):
#     if word == word[::-1]:
#         return True
#     return False
# print(is_pallindrome("himanshu"))
# print(is_pallindrome("121"))

# num = int(input("enter number:-"))
# reverse =0
# reminder=0
# temp = num

# while (num>0):
#     reminder = num % 10
#     reverse = reverse*10+reminder
#     num = num//10
# print(f"reversed value {reverse}")
# if reverse == temp:
#     print("is_pallindrome")
# else:
#     print("is_pallindrome")

def is_pallindrome(word):
    return word == word[::-1]
print(is_pallindrome("naman"))
print(is_pallindrome("madam"))
print(is_pallindrome("vidhi"))


