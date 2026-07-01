import random

def hangman():
    words = ["apple", "tiger", "house", "chair", "water"]

    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("Welcome to Hangman!")

    while wrong_guesses < max_wrong:
        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)

        # Check if word is completed
        if "_" not in display:
            print("Congratulations! You guessed the word:", word)
            return

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Correct!")
        else:
            guessed_letters.append(guess)
            wrong_guesses += 1
            print("Wrong guess!")
            print("Remaining chances:", max_wrong - wrong_guesses)

    print("\nGame Over!")
    print("The word was:", word)

# Run the game
hangman()