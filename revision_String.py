#string
name = "vidhi"
print(name)
#string indexing
print(name[3])
print(name[-2])
#string slicing
print(name[0:3:2])
#take user inputs
name=input("enter your name:-")
print(name)
#take two user inputs
name,age,colr=input("enter name,age,colr seprated by comma:-").split(",")
print("name,age and colr:-",name,age,colr)
#len function
print(len(name))
#lower , upper , title method
print(name.lower())
print(name.upper())
print(name.title())
#find , replace , center method
print(name.find("i"))
print(name.replace("i","h"))
print(name.center(9,"*"))
#strings are immutable
# name[1]="p"
# print(name)


