import random

player1 = input("Enter Your Choice(r,p,s): ")
playerChoices = ["r", "p", "s"]
player2 = random.choice(playerChoices)
if player1 == player2:
    print("Its a Tie")
elif player1 == 'r' and player2 == 'p':
    print(f"You choose {player1}, bot choose {player2}. You lost.")
elif player1 == 'p' and player2 == 's':
    print(f"You choose {player1}, bot choose {player2}. You lost.")
elif player1 == 's' and player2 == 'r':
    print(f"You choose {player1}, bot choose {player2}. You Lost.")
elif player1 == 's' and player2 == 'p':
    print(f"You choose {player1}, bot choose {player2}. You Won.")
elif player1 == 'p' and player2 == 'r':
    print(f"You choose {player1}, bot choose {player2}. You Won.")
elif player1 == 'r' and player2 == 's':
    print(f"You choose {player1}, bot choose {player2}. You Won.")
else:
    print("Invalid input.")
