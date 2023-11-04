# Ans: To execute a block of code when a condition is false

# str1 = 'Australia'
# if ('a'or 'e'or'i'or'o'or'u') in str1:
#     print("Vowel is present")
# else:
#     print("Vowel is not present")

# string = input("enter here:-")
# vowels = ('AEIOUaeiou')
# vowels_find = False
# for char in string:
#     if char in vowels:
#         vowels_find = True
#         break
# if vowels_find :
#     print("present vowels")
# else:
#     print("not present")
# text = input("enter here:-")
# vowels ='AEIOUaeiou'
# count=0
# for char in text:
#     if char in vowels:
#         count += 1
# print("number of vowels",count)


# input_string = "There are many operations that can be performed with strings"
# words = input_string.split()
# longest_word = ""
# max_length = 0
# for word in words:
#     if len(word) > max_length:
#         max_length = len(word)
#         longest_word = word
# print("The longest word is:", longest_word)

# assignments
# 1. remove the space from string = "HellowWorld"
# string = "Hello World!"
# # spaces = string.replace(" ", "")
# # print(spaces)

# string = "Hel lo Wor ld!"
# spaces = ""

# for char in string:
#     if char != " ":
#         spaces += char

# print(spaces)


# 2.find the maximum occurence of a particular chracter in a string "Mississipie"

input_string = "Miississipe"

max_char = ""
max_count = 0

for char in input_string:
    count = input_string.count(char)
    if count > max_count:
        max_char = char
        max_count = count

print(max_char,max_count)


# def reverse_string(input_str):
#     reversed_str = ""
#     for i in range(len(input_str) - 1, -1, -1):
#         reversed_str += input_str[i]
#     return reversed_str

# input_str = "programming python"
# reversed_str = reverse_string(input_str)
# print(reversed_str)


# DECORATOR
# def decor_result(result_function):
#     def distinction(a,b):
#         print(a*b)       
#         result_function(a,b)
        
#     return distinction

# @decor_result
# def result(c,d):
#     print(c+d)
        
# result(23,40)