import random
from pathlib import Path
from collections import Counter

HANGMAN = [
'  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========',
'  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========',
'  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========',
'  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========',
'  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========',
'  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========='
]

WORDLIST = Path(r"wordlist.txt")
words = [
    word.lower()
    for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")
    ]

def goodmessage():
    messages = ['Good guess! You\'re getting closer!', 'Great job! Keep it up!', 'Awesome! So much closer to saving Tim!']
    return random.choice(messages)

def guess(tries, word):
    lettersguessed = []
    correctguesses = []
    guessed = False
    print(f'Guess a letter! You get six tries but they aren\'t used when you get it right.')
    print(f'Your word is {len(word)} letters long.')
    track = 0
    hang = HANGMAN[track]

    while tries >= 0 and hang != HANGMAN[len(HANGMAN)-1] and not guessed:
        guess = input('Guess: ').lower()

        if type(guess) != str or not guess.isalpha():
            print('You need to input a letter! Try again')
            continue
        elif len(guess) > 1:
            print('Just ONE letter! Try again')
            continue
        elif guess in lettersguessed:
            print('Guess a letter you haven\'t guessed before silly!')
            continue
        
        if guess in word:
            k = word.count(guess)
            for i in range(k):
                lettersguessed.append(guess)
                correctguesses.append(guess)
            if Counter(correctguesses) != Counter(word):
                print(goodmessage())
        else:
            tries -= 1
            print(f'Oh no! Tim! Be careful you have {tries} tries left!')
            lettersguessed.append(guess)
            hang = HANGMAN[track]
            track += 1
            
            print(hang)
        
        for char in word:
            if char in correctguesses and Counter(correctguesses) != Counter(word):
                print(char, end = ' ')
            elif Counter(correctguesses) == Counter(word):
                print(f'Yay! The word was {word}!')
                print('You saved Tim! Congratulations')
                guessed = True
                break
            else:
                print("_", end = ' ')
        print()
                        
    if tries >= 0 and Counter(correctguesses) != Counter(word):
        print('Oh no! You lost! Tim is gone!')
        print(f'The word was {word}!')
        print(HANGMAN[len(HANGMAN)-1])
    

print('Welcome to Hangman! You guess letters and we tell you if it\'s right.')
print('Be careful! Everytime you guess wrong Tim\'s body part is added to the stage!')
print('  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========')
print('Try to save Tim!')

word = random.choice(words)
tries = 6
guess(tries,word)
play = input('Do you wany to play again? ').lower()
while play == 'yes' or play == 'y':
    print("Welcome Back!")
    word = random.choice(words)
    tries = 6
    guess(tries,word)
    play = input('Do you wany to play again? ').lower()



