#MODIFY NUMBER GUSSING GAME

winning_number=43
guess=1
number=int(input("enter number b/w 1-100:-"))
game_over=False

while not game_over:
    if number == winning_number:
        print(f"you win,and you guess this number {guess} times")
        game_over=True
    else:
        if number < winning_number:
            print("too low")
            guess+=1
            number=int(input("guess again...."))
        else:
            print("too high")
            guess+=1
            number=int(input("guess again...."))