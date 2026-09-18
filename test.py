import random

secret = random.randint(1, 50)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess a number between 1 and 50: "))
    attempts += 1

    if guess == secret:
        print(f"🎉 Congratulations! You guessed the secret number {secret}!")
        break
    else:
        diff = abs(secret - guess)

        if diff >= 20:
            print("🧊 Ice cold!")
        elif diff >= 10:
            print("🥶 Cold!")
        elif diff >= 5:
            print("🌡️ Warm!")
        else:
            print("🔥 Hot!")

        remaining_lives = max_attempts - attempts
        if remaining_lives > 0:
            print("Remaining lives: ", end="")
            for _ in range(remaining_lives):
                print("❤️ ", end="")
            print("\n")

if attempts == max_attempts and guess != secret:
    print(f"❌ Game over! You ran out of attempts. The secret number was {secret}.")