import random
guess = int(input("Guess a number from 1 to 10: "))
answer = random.randint(1, 2)
if guess > 10:
    print("GUESS FROM 1 TO 10.")
elif guess == answer:
    print("You guessed correctly.")
else:
    print("You guessed incorrectly.")
    print("The correct answer is " + str(answer))
