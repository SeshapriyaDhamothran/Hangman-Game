import random

# List of words for the game
word_list = ['python', 'developer', 'hangman', 'program', 'computer', 'keyboard', 'function', 'variable']

# Choose a random word
word_to_guess = random.choice(word_list)
word_length = len(word_to_guess)
display = ['_'] * word_length  # Initial display of blanks

attempts = 6  # Number of allowed wrong guesses
guessed_letters = []

print("Welcome to Hangman Game!")
print("Guess the word:")

while attempts > 0 and '_' in display:
    print("\n" + " ".join(display))
    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word_to_guess:
        print(f"Good job! '{guess}' is in the word.")
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                display[i] = guess
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")

# Game result
if '_' not in display:
    print("\nCongratulations! You guessed the word:", word_to_guess)
else:
    print("\nGame Over! The word was:", word_to_guess)

