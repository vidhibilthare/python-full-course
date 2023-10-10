# sum of naturals number
# ask a user for naturals number(n)
# print total 1 to n 
user_input=int(input("enter natural number here:-"))
sum = 0
i = 1
while i <= user_input:
    sum = sum + i
    i += 1
print(f"total of n natirals number {sum}")