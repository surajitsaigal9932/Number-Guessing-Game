import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("Select a difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)\n")

    while True:
        try:
            difficulty = int(input("Enter your choice (1/2/3): "))
            if difficulty == 1:
                max_attempts = 10
                break
            elif difficulty == 2:
                max_attempts = 7
                break
            elif difficulty == 3:
                max_attempts = 5
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Please enter a number (1/2/3).")

    random_number = random.randint(1, 100)
    attempts = 0

    print("\nGuess the number between 1 and 100:")
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
            if guess < 1 or guess > 100:
                print("Invalid input! Please guess a number between 1 and 100.\n")
                continue
            attempts += 1

            if guess == random_number:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!\n")
                return True
            elif abs(guess - random_number) <= 5:
                print("🔥 You're very close! Try again.\n")
            elif guess < random_number:
                print("🔼 Guess a Higher number.\n")
            else:
                print("🔽 Guess a Lower number.\n")
        except ValueError:
            print("Invalid input! Please enter a number.\n")

    print(f"💔 Game Over! The correct number was {random_number}.\n")
    return False

def main():
    score = {"wins": 0, "losses": 0}
    while True:
        play = input("Do you want to play the Number Guessing Game? (yes/no): ").strip().lower()
        if play == 'yes':
            if play_game():
                score["wins"] += 1
            else:
                score["losses"] += 1
        elif play == 'no':
            print("\nThank you for playing!")
            print(f"Your final score: {score['wins']} Wins, {score['losses']} Losses")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.\n")

if __name__ == "__main__":
    main()
