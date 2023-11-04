# exception handling
# try except else finally
while True:
    try:
        age = int(input("enter your age"))
        break
    except ValueError:
        print("may be you entered string instead of number , try again..")
    except:
        print('unexpected error..')
if age < 18:
    print("you can not play game")
else:
    print("you can play game")

# exceptions-wo error jo hmare pass execution k time aati hain
