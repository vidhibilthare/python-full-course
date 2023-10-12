# common elements finder function
# define a function which take 2 lists as input and return 
# a list
# which contains common elements of both lists
# example--->
# input-->[1,2,3,4],[1,2,4,5]
#output-->[1,2,4]

def common_num(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output
print(common_num ([1,2,3,4],[1,2,4,5]))