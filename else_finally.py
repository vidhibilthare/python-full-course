# else and finally clause in exception handling
while True:
    try:
        number = int(input("enter number here:-"))
        
    except ValueError:
        print('you did not entered interger')
    except:
        print('unexpected error...')
    else:
        print(f'user input{number}')
        break
    finally:
        print('finally block....!!')