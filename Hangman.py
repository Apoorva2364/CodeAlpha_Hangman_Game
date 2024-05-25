import random

def get_random_word():
    words = ['python', 'java', 'kotlin', 'javascript', 'hangman']
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f'Word: {display}')

def hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        display_current_state(word, guessed_letters)
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
