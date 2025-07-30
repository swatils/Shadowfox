import random
from collections import Counter

# List of possible words
someWords = '''BMW audi porsche lamborghini 
RollsRoyce mercedesbenz toyota hyundai bugatti volkswagen McLaren 
tata jaguar ford volvo landrover ferrari'''.split()

# Randomly choose a secret word
word = random.choice(someWords)

if __name__ == '__main__':
    print(" Guess the word! HINT: It's a car.")

    # Print underscores for the word
    print("_ " * len(word))

    letterGuessed = ''      # Store all guessed letters
    chances = len(word) + 2 # Extra chances
    flag = 0                # Win flag

    try:
        while chances > 0 and flag == 0:
            print(f"\nRemaining chances: {chances}")
            guess = input("Enter a letter: ").lower().strip()

            #  Validate the guess
            if not guess.isalpha():
                print(" Enter only a LETTER!")
                continue
            elif len(guess) > 1:
                print(" Enter only a SINGLE letter!")
                continue
            elif guess in letterGuessed:
                print(" You already guessed that letter.")
                continue

            # Add guessed letter
            letterGuessed += guess

            #  Print current progress of the word
            current_progress = ""
            for char in word:
                if char in letterGuessed:
                    current_progress += char + " "
                else:
                    current_progress += "_ "

            print(current_progress.strip())

            #  Check if guessed completely
            if all(char in letterGuessed for char in word):
                print("\n Congratulations! You guessed the word:", word)
                flag = 1
                break

            chances -= 1  # reduce chances after each guess

        # If out of chances
        if flag == 0:
            print("\n You lost! The word was:", word)

    except KeyboardInterrupt:
        print("\n Game stopped. Bye!")
