# intro to *args

# make flexible functions

#operator

#*args

def total(a,b):
    return a+b
print(total(2,3))


def all_total(*args):
    print(args)
    print(type(args))
all_total(1,2,3,4,5,6,7,8,9,10)

def total(*arg):
    total=0
    for nums in arg:
        total += nums
    return total
print(total(1,2,3,4))

