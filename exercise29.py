# define generator functions
# take one number as argument
# generate sequence of even number from 1 to that number
# 5-->2,4
# 7-->2,4,6
def even_generater(n):
    for num in range(1,n+1): #for num in range(2,n+1,2)
        if num%2==0:            #yield(num)
            yield(num)
even_nums =even_generater(20)
for num in even_nums:
    print(num)

