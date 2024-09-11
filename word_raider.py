import random

game_title = "Word Raider"
# Set up the list of words to choose from
word_bank = []

with open("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())

# Pick a random word from the list
word_to_guess = random.choice(word_bank)

# Set up the game variables
misplaced_guesses = []
incorrect_guesses = []
max_turns = 7
turns_taken = 0

# Display the initial game state
print("Welcome to", game_title)
print("The word has", len(word_to_guess), "letters.")
print("You have", max_turns - turns_taken, "turns left.")

while turns_taken < max_turns:
    # Get the player's guess
    guess = input("Guess a word: ").lower()

    # Check if the guess length equals 5 letters and is all alpha letters
    if len(guess) != len(word_to_guess) or not guess.isalpha():
        print("Please enter 5-letter word.")
        continue

    # Check each letter in the guess against the word's letters
    index = 0
    for c in guess:
        if c == word_to_guess[index]:
            print(c, end=" ")
            if c in misplaced_guesses:
                misplaced_guesses.remove(c)
        elif c in word_to_guess:
            if c not in misplaced_guesses:
                misplaced_guesses.append(c)
            print("_", end=" ")
        else:
            if c not in incorrect_guesses:
                incorrect_guesses.append(c)
            print("_", end=" ")
        index += 1

    print("\n")
    print("Misplaced letters: ", misplaced_guesses)
    print("Incorrect letters: ", incorrect_guesses)
    turns_taken += 1

    # Check if the player has won
    if guess == word_to_guess:
        print("Congratulations, you win!")
        break

    # Check if the player has lost
    if turns_taken == max_turns:
        print("Sorry, you lost. The word was", word_to_guess)
        break

    # Display the number of turns left and ask for another guess
    print("You have", max_turns - turns_taken, "turns left.")