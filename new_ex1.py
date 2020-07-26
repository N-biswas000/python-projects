winning_number=6
guess_number=int(input("Enter Your Guess number"))
if winning_number==guess_number:
    print("You Won!")
elif winning_number>guess_number:
    print("Too Low Sorry")
else winning_number<guess_number:
    print("Too High Sorry!")
