import random
number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("enter the guessing number:"))
    attempts += 1

    if guess == number:
        print("Correct guess!")
        print("You guessed attempts:", attempts)
        break
    elif guess < number:
        print("guess lower")
    else:
        print("guess higher")