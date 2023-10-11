#DRY PRINCIPLEOF CODING
# DRY-dont repeat yourself
winning_number=55
guess=1
number=int(input("guess a number b/w 1-100-"))
game_over=False

while not game_over:
    if number == winning_number:
        print(f"you win, and you guessed this number IN {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print("too low")
        else:
            print("too high")
        
        guess+=1
        number = int(input("guess again :"))
