# python custom exceptions
# why custom Exceptions
# to increase the readability of code

# example
def validate(name):
    if len(name)<8:
        raise ValueError('name is too short')
user_name=input("enter name here:-")
validate(user_name)
print(f'hello {user_name}')