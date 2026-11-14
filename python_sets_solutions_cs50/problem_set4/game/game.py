from random import randint

while True:
    x = input("Level: ")
    if x.isdigit() and int(x) > 0:
        break

x = int(x)
y = randint(1, x)

while True:
    guess = input("Guess: ")

    if guess.isdigit() and int(guess) > 0:
        guess = int(guess)
    else:
        continue

    if guess < y:
        print("Too small!")
    elif guess > y:
        print("Too large!")
    else:
        print("Just right!")
        break
