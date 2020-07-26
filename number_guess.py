winning_number=43
guess=1
game_over=False
number=int(input("Enter a number between 1 to 100 :"))
while game_over==False:
    if winning_number==number:
        print(f"You Won!, and you win this with {guess} times ")
        game_over=True
    else:
        if winning_number > number:
            print("Too Low!")
        else:
            print("Too High")
            
        guess+=1
        number=int(input("guess again :"))