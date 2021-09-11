# Problem Set 2, hangman.py
# Name: Yuhan Liu
# Collaborators: Jiaheng Xu
# Time spent:3hrs

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    empty_word = []
    list_secret_word = list(secret_word)

    for i in range(len(secret_word)):
        empty_word.append('_')
    for letter in letters_guessed:
        if letter in list_secret_word:
            count = 0
            for each_letter in list_secret_word:
                if each_letter == letter:
                    empty_word[count] = letter
                count += 1

    return ''.join(empty_word)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    remain_letters = list(string.ascii_lowercase)

    if not letters_guessed:
        return string.ascii_lowercase

    for letter in letters_guessed:
        remain_letters.remove(letter)

    return ''.join(remain_letters)


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    """
    guesses = 6
    warnings = 3
    letters_guessed = []
    current_word = get_guessed_word(secret_word, letters_guessed)
    list_secret_word = list(secret_word)
    vowel = 'aeiou'

    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long')
    print('-------------')
    print(f'You have {warnings} warnings left.')

    while guesses > 0:
        available_letters = get_available_letters(letters_guessed)
        print(f'You have {guesses} guesses left.')
        print(f'Available letters: {available_letters}')

        letter_guessed = input('Please guess a letter: ')
        while len(letter_guessed) > 1:
            print('This is an invalid input, please try again.')
            letter_guessed = input('Please guess a letter: ')
        letter_guessed.lower()

        if letter_guessed in list_secret_word:
            letters_guessed.append(letter_guessed)
            current_word = get_guessed_word(secret_word, letters_guessed)
            print(f'Good guess: {current_word}')
        elif not letter_guessed.isalpha():
            if warnings > 0:
                warnings -= 1
                print(f'Oops! That is not a valid letter. '
                      f'You have {warnings} warnings left: {current_word}')
            else:
                guesses -= 1
                print(f'Oops! That is not a valid letter. You have no warnings '
                      f'left so you lose one guess: {current_word}')
        elif letter_guessed in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print(f"Oops! You've already guessed that letter. "
                      f"You now have {warnings} warnings left: {current_word}")
            else:
                guesses -= 1
                print(f"Oops! You've already guessed that letter. You have no warnings "
                      f"left so you lose one guess: {current_word}")
        else:
            letters_guessed.append(letter_guessed)
            if letter_guessed in list(vowel):
                guesses -= 2
            else:
                guesses -= 1
            print(f'Oops! That letter is not in my word: {current_word}')

        print('-------------')

        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses * len(secret_word)
            print('Congratulations, you won!')
            print(f'Your total score for this game is: {total_score}')
            return

    print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
    return


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    """
    if len(my_word) != len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if (my_word[i] != '_') and (my_word[i] != other_word[i]):
                return False
    return True


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    matched_wordlist = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched_wordlist.append(word)
            matched_wordlist.append(' ')
    if matched_wordlist:
        print(''.join(matched_wordlist))
    else:
        print('No matches found')


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    """
    guesses = 6
    warnings = 3
    letters_guessed = []
    current_word = get_guessed_word(secret_word, letters_guessed)
    list_secret_word = list(secret_word)
    vowel = 'aeiou'

    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long')
    print('-------------')
    print(f'You have {warnings} warnings left.')

    while guesses > 0:
        available_letters = get_available_letters(letters_guessed)
        print(f'You have {guesses} guesses left.')
        print(f'Available letters: {available_letters}')

        letter_guessed = input('Please guess a letter: ')
        while len(letter_guessed) > 1:
            print('This is an invalid input, please try again.')
            letter_guessed = input('Please guess a letter: ')
        letter_guessed.lower()

        if letter_guessed in list_secret_word:
            letters_guessed.append(letter_guessed)
            current_word = get_guessed_word(secret_word, letters_guessed)
            print(f'Good guess: {current_word}')
        elif not letter_guessed.isalpha():
            if letter_guessed != '*':
                if warnings > 0:
                    warnings -= 1
                    print(f'Oops! That is not a valid letter. '
                          f'You have {warnings} warnings left: {current_word}')
                else:
                    guesses -= 1
                    print(f'Oops! That is not a valid letter. You have no warnings '
                          f'left so you lose one guess: {current_word}')
            else:
                print('Possible word matches are:')
                show_possible_matches(current_word)

        elif letter_guessed in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print(f"Oops! You've already guessed that letter. "
                      f"You now have {warnings} warnings left: {current_word}")
            else:
                guesses -= 1
                print(f"Oops! You've already guessed that letter. You have no warnings "
                      f"left so you lose one guess: {current_word}")
        else:
            letters_guessed.append(letter_guessed)
            if letter_guessed in list(vowel):
                guesses -= 2
            else:
                guesses -= 1
            print(f'Oops! That letter is not in my word: {current_word}')

        print('-------------')

        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses * len(secret_word)
            print('Congratulations, you won!')
            print(f'Your total score for this game is: {total_score}')
            return

    print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
    return


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__oldmain__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

if __name__ == "__main__":
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
