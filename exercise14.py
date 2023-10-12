# define a function which will take list as a arguments 
# and this function will return a reversed list
# example->[1,2,3,4]-->[4,3,2,1]
# ['word1','word2','word3']--->['word3','word2','word1']
# note-->you will do this with reverse method or [::-1]

# but try to do this with the
#  help of append and return method

# def reversed_list(l):
#     l.reverse()
#     return l
# def reversed_list(l):
#     return l[::-1]

def reverse_list(l):
    r_list = []
    for i in range(len(l)):
        popped_item = l.pop()
        r_list.append(popped_item)

    return r_list


numbers=[1,2,3,4]
print(reverse_list(numbers))

