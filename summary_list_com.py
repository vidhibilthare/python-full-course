# list comprehension summary
# square = []
# for i in range(1,11):
#     square.append(i**2)
# print(square)


# square = [i**2 for i in range(1,11)]
# print(square)


# even_num = [i for i in range(1,11) if i%2==0 ]
# print(even_num)

# new_list = [i**2 if i%2==0 else -i for i in range(1,11)]
# print(new_list)

# nl = [[1,2,3],[1,2,3],[1,2,3]]
# new_list = [[i for i in range(1,4)] for j in range(3)]
# print(new_list)

l2 = []
for j in range(3):
    l2.append([1,2,3])
print(l2)
