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


input_string = "There are many operations that can be performed with strings"
words = input_string.split()
longest_word = ""
max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word
print("The longest word is:", longest_word)