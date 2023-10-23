def multipy(*arg):
    multiple =1
    print(arg)
    for i in arg:
        multiple*=i
    return multiple


nums =[1,2,3,4]
print(multipy(*nums)) # (* lagane s sab kuch unpack ho jaega)