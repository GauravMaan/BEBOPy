import random
gu = random.randint(1, 100)
attempts = 0
print("Welcome to 'Guess the Number'! Try to guess the number between 1 and 100.")
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < gu:
        print("Too low. Try again!")
    elif guess > gu:
        print("Too high. Try again!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
