'''Modify your Hangman game, so a word is selected randomly from
a list of words.'''




# NEED TO FIGURE OUT HOW TO HAVE LINES APPEAR AFTER CORRECT GUESS OF THE LETTERS(Fig a)

import random #using random module built in to python


def hangman():
    word_list = ["anime", "code", "steak", "coffee", "headphones", "videogames", "eva", "aaron", "james", "miles"] #can edit so python can pick random words from list
    random_number = random.randint(0, 9) #.ranint() is a function that will choose a random number on your list
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["", "________     ", "|      |     ", "|      0    ", "|     /|\    ", "|     / \    ", "|"]
    rletters = list(word)
    letter_board = ["__"] * len(word)# Fig a here or below. Test to see how this works
    win = False
    print('Welcome to Hangman!')
    while wrong_guesses < len(stages) -1:
        print('\n')
        guess = input("Guess a letter")
        if guess in rletters:
            character_index = rletters.index(guess)
            letter_board[character_index] = guess
            rletters[character_index] = '$'
        else:
            wrong_guesses += 1
            print((' '.join(letter_board)))
            print('\n'.join(stages[0: wrong_guesses + 1]))
            if '__' not in letter_board:
                print('YOU WIN!!! The word was:')
                print(' '.join(letter_board))
                win = True
                break


    if not win:# the answer was being included while getting wrong answer, fix was to have the loop with correct space/indent
        print('\n'.join(stages[0: wrong_guesses]))
        print('AAAWWWWW TAKE THE L!!!!! The word was: {}'.format(word))

hangman()
