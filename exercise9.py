# ask a user for name
# Example:- vidhi bilthare
# print count of each word
# output:
   

# user_name = input("enter your name")
# vidhi shukla
# name.count("v")-1 name.count(name[0])
# name.count("i")-2 name.count(name[1])
# name.count("d")-1 name.count(name[2])
# name.count("h")-2 name.count(name[3])
# name.count("s")-1 name.count(name[4])
# name.count("u")-1 name.count(name[5])
# name.count("k")-1 name.count(name[6])
# name.count("l")-1 name.count(name[7])
# name.count("a")-1 name.count(name[8])
#output
# v-1
# i-2
# d-1
# h-1
# i-2
name=input("enter your name:-")
i=0
temp_var=""
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]}:{name.count(name[i])}")
    i+=1