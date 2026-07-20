import random
"""Assigning the Game's Words"""
def get_words():
    words = ["Mango","Banana","Apple","Orange","Grapes"]
    return random.choice(words)
def representation(word,Guessed): 
    for n in range(len(Guessed)):
        print(word[n], end=" ")
    for i in range(len(Guessed),len(word)):
        print("_", end=" ")
"""CORRECT OR NOT"""
def check_guess():
    word = get_words()
    guessed_letters = []
    attempts = 6
    print("Choose a Letter....FIRST LETTER'S Capital and others are small letters. YOU Have", attempts, "guess attempts left")
    
    while attempts > 0 and len(guessed_letters) < len(word):
        representation(word, guessed_letters)
        guess = input("Enter your guess: ")
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in word:
            print("Correct Guess!")
            guessed_letters.append(guess)
        else:
            print("Incorrect Guess. Try Again!")
            attempts -= 1
            print("YOU HAVE", attempts, "guess attempts left")
    if len(guessed_letters) == len(word):
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Sorry, you're out of attempts. The word was:", word) 
check_guess()