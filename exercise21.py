# users={
#     'name':'himanshu',
#     'age':27,
#     'wife':'vidhi',
#     'color':'red'
# }
user={}
name = input("enter your name:-")
age = input('enter age:-')
wife=input('enter ours wife name:-')
color=input("enter color:-").split(',')
user['name']=name
user['age']=age
user['wife']=wife
user['color']=color 
# print(user)
for key, value in user.items():
    print(f"{key} : {value}")