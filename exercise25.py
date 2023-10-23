# define a functions
# inputs
#nums,iterable(tuple,list) containing numbers as args


# example 
# nums = [1,2,3]
# to_power(3,*nums)

# output 
# lists-->[1**3, 8 ,27]

# if user didnt pass any args then give a user a message 
# 'hey you didnt pass arg'

# else
# return list

# note-->Use list comprehension

# l=[]
# if l:
#     print('no empty!!!')
# else:
#     print('empty')

# if len(l)>0:
#     print('no empty')
# else:
#     print(' empty')

def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return 'you didnt pass any args..'
    
nums = [1,2,3]
print(to_power(2,*[2,3]))