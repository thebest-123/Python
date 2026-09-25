import random

# Generate secret number (or set fixed like secret = 27)
secret = random.randint(1, 50)

attempts = 5
won = False

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50. You have 5 attempts.")

while attempts > 0 and not won:
    guess = int(input("\nEnter your guess: "))

    if guess == secret:
        print("🎉 Congratulations! You guessed the secret number!")
        won = True
    else:
        attempts -= 1
        
        # Calculate distance to determine hint
        difference = abs(secret - guess)

        if difference > 20:
            print("Hint: 🧊 ice cold")
        elif difference > 10:
            print("Hint: 🥶 cold")
        elif difference > 5:
            print("Hint: 🌡️ warm")
        else:
            print("Hint: 🔥 hot")

        if attempts > 0:
            # For loop to print remaining hearts
            print("Remaining lives: ", end="")
            for _ in range(attempts):
                print("❤️ ", end="")
            print()

# Loss message if attempts run out
if not won:
    print(f"\nGame Over! You ran out of attempts. The secret number was {secret}.")