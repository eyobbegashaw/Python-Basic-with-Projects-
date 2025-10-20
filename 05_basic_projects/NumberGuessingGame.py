import random

# Generate random number
secret_number = random.randint(1, 10)
attempts = 0

print("Guess the number between 1 and 10!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break