import random

# List of words
words = [
    "apple", "banana", "orange", "mango", "grape",
    "python", "computer", "keyboard", "network",
    "developer", "algorithm", "database", "software"
]

# Hangman stages
hangman_stages = [
    """
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """
]


def play_hangman():
    word = random.choice(words)
    display = ["_"] * len(word)
    guessed_letters = []
    attempts = 6

    print("\n🎮 Welcome to Hangman Game!")

    while attempts > 0 and "_" in display:
        print(hangman_stages[attempts])
        print("Word:", " ".join(display))
        print("Guessed Letters:", " ".join(guessed_letters))
        print("Attempts Left:", attempts)

        guess = input("Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter only one alphabet.")
            continue

        # Duplicate guess
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Correct guess
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
            print("✅ Correct Guess!")
        else:
            attempts -= 1
            print("❌ Wrong Guess!")

    # Final result
    if "_" not in display:
        print("\n🎉 Congratulations! You Won!")
        print("The word was:", word)
    else:
        print(hangman_stages[0])
        print("\n💀 Game Over!")
        print("The word was:", word)


# Main program
play_again = "yes"

while play_again == "yes":
    play_hangman()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

print("\nThank you for playing Hangman!")