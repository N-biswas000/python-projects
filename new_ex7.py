import random
winning_number=random.randint(1,100)
guess=1
number=int(input("Enter a number between 1 to 100 :"))
game_over=False
while not game_over:
    if winning_number==number:
        print(f"You Won!, and you guess this no {guess} times")
        game_over=True
    else:
        if winning_number < number:
            print("Too High!")
            guess += 1
            number=int(input("Guess again! :"))
        else:
            print("Too Low!")
            guess += 1
            number=int(input("Guess again! :"))
        
            
        
