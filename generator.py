# genaraters
# generaters are itretors

# iterator/itrable
l=[1,2,3,4]#itrable
# for i in l:
    # print(i)
# i=iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for num in map(lambda a:a*2,l):
#     print(num)#iterator

# create yoyr first generater with generator functions
# generator functions
# generator comprehension

def nums(num):
    for i in range(1,num+1):
        yield(i)

numbers = list(nums(10))
for nums in numbers:
    print(nums)

for nums in numbers:
    print(nums)

# memory-->list-->list create hone m time lgega phir memory main store hogi
#generator-->kabhi b puri sequence ek sth generate nhi krta jb tk koi demand nhi hoti
# no memory sorted
