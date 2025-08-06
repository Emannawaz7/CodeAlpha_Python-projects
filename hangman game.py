import random

# Predefined list of 5 words
words = ["apple", "water", "eman", "pakistan", "happy"]

# Randomly select a word
word = random.choice(words)
guessed_word = ["_"] * len(word)
guessed_letters = []
tries = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have", tries, "incorrect guesses allowed.\n")

while tries > 0 and "_" in guessed_word:
    print("Current word:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter only one valid letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
        for index, letter in enumerate(word):
            if letter == guess:
                guessed_word[index] = guess
    else:
        tries -= 1
        print("❌ Wrong guess. Tries left:", tries)

# End of game messages
if "_" not in guessed_word:
    print("\n Congratulations! You guessed the word:", word)
    print("\n Game Over! The word was:", word)
