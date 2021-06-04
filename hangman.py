# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

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

wordlist = load_words()

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
#wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE  DELETE "pass"
    for w in secret_word :
        if w not in letters_guessed:
            return False
        else :
            pass
    return True
        
            
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    k = 0
    list = []
    while k!= len(secret_word):
        list.append('_')
        k = k + 1
    for w in letters_guessed :
        for k in secret_word:
            if w == k :
                list[secret_word.index(k)] = w
                secret_word = secret_word[0:secret_word.index(k)]+'.'+secret_word[secret_word.index(k)+1:]
                
            else:
                pass
            
            
    return ''.join(list)
    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_list = []
    for k in string.ascii_lowercase :
        letters_list.append(k)
    for w in letters_list :
        for k in letters_guessed :
            if w == k:
                 letters_list.pop(letters_list.index(w))
            else:
                pass
    return "".join(letters_list)
    
    

def hangman(secret_word):
        
    k = 0
    list = []
    while k!= len(secret_word):
        list.append('_')
        k = k + 1
    lists= ''.join(list)
    letters_guessed = []
    print('Welcome to the game Hangman')
    secret_word = choose_word(load_words())
    print(f'I am thinking of a word that is {len(secret_word)} letters long..........')
    length = len(secret_word)+ 3
    vowels = ['a','e','i','o','u']
    warnings=4
    unique= len(secret_word)
    while length!= 0 :
        continue_while = ''
        print(f'you have {length } guesses left ')
        print(f'available letters are {string.ascii_lowercase}')
        print('please guess a letter : ') 
        letter = input()
        if letter.isalpha() :
            for l in letters_guessed:
                if l == letter.lower():
                    continue_while = True
                    print('letter has already entered try another letter...')
                    break

            if continue_while:
                continue
            letters_guessed.append(letter.lower())
            for l in vowels :
                if l == letter.lower():
                    v=True
                    break
                else:
                    v=False
                    continue
           # print(letters_guessed)
            if v:
                if get_guessed_word(secret_word,letters_guessed)== lists:
                    print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}')
                    length = length -2
                else:
                    print(f'good guess : {get_guessed_word(secret_word,letters_guessed)}')
                    lists = get_guessed_word(secret_word,letters_guessed)  
                    if is_word_guessed(secret_word, letters_guessed):
                        print(f'you have won the game')
            else:
                if get_guessed_word(secret_word,letters_guessed)== lists:
                    print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}')
                    length = length -1
                else:
                    print(f'good guess : {get_guessed_word(secret_word,letters_guessed)}')
                    lists = get_guessed_word(secret_word,letters_guessed)
                    if is_word_guessed(secret_word, letters_guessed):
                        print(f'you have won the game')
                        break
        elif warnings>0:
            print ('you have to enter alphbets Oops! That is not a valid letter')
            warnings = warnings -1
            print (f'warnings left {warnings} and word is {lists} ')
            continue
        else:
            for l in letters_guessed:
                if l == letter.lower():
                    continue_while = True
                    print('letter has already entered try another letter...')
                    break  
            if continue_while:
                continue
            letters_guessed.append(letter.lower())
           # print(letters_guessed)
            if get_guessed_word(secret_word,letters_guessed) == lists :
                print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}')
                length = length -1
            else:
                print(f'good guess : {get_guessed_word(secret_word,letters_guessed)}')
                lists = get_guessed_word(secret_word,letters_guessed)
                if is_word_guessed(secret_word, letters_guessed):
                    print('you have won the game')
    if is_word_guessed(secret_word, letters_guessed):
        print('you have won the game')               
    else:
        print(f'you have lost the game try again\n the word is {secret_word}')

    


    
    
    
    

    



        


# FILL IN YOUR CODE HERE AND DELETE "pass"
    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
        
    '''
    for l in my_word:
        if l  in other_word :
            return True
        elif l == '_':
            return True
    else : return False

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
	
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    lis = []
    for q in wordlist:
    
        if len(my_word) == len(q):
            lis.append(q)
        else:
            pass
    m = []
    a = list(my_word)
    for l in a:
        if l != "_":
            m.append(a.index(l))
            a[a.index(l)]='_'
    print(m)
    l = []
    for s in lis:
        k = 0
        t = 0
        while k != len(m):
            if my_word[m[k]] in s[m[k]]:
                t = t+1
            k = k +1
        if t == len(m):
            l .append(s)
    print(l)
    return True    #E HERE AND DELETE "pass"
    



def hangman_with_hints(secret_word):
    
    
    
    '''
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
    '''
    k = 0
    list = []
    while k!= len(secret_word):
        list.append('_')
        k = k + 1
    my_word= ''.join(list)
    letters_guessed = []
    print('Welcome to the game Hangman')
    secret_word = choose_word(load_words())
    print(f'I am thinking of a word that is {len(secret_word)} letters long..........')
    length = len(secret_word)+ 3
    vowels = ['a','e','i','o','u']
    warnings=4
    unique= len(secret_word)
    while length!= 0 :
        continue_while = ''
        print(f'you have {length } guesses left ')
        print(f'available letters are {string.ascii_lowercase}')
        print('please guess a letter : ') 
        letter = input()
        if letter.isalpha() :
            for l in letters_guessed:
                if l == letter.lower():
                    continue_while = True
                    print('letter has already entered try another letter...')
                    break

            if continue_while:
                continue
            letters_guessed.append(letter.lower())
            for l in vowels :
                if l == letter.lower():
                    v=True
                    break
                else:
                    v=False
                    continue
           # print(letters_guessed)
            if v:
                if get_guessed_word(secret_word,letters_guessed)== my_word:
                    print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}')
                    length = length -2
                else:
                    print(f'good guess : {get_guessed_word(secret_word,letters_guessed)}')
                    my_word= get_guessed_word(secret_word,letters_guessed)  
                    if is_word_guessed(secret_word, letters_guessed):
                        print(f'you have won the game')
            else:
                if get_guessed_word(secret_word,letters_guessed)== my_word:
                    print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}')
                    length = length -1
                else:
                    print(f'good guess : {get_guessed_word(secret_word,letters_guessed)}')
                    lists = get_guessed_word(secret_word,letters_guessed)
                    if is_word_guessed(secret_word, letters_guessed):
                        print(f'you have won the game')
                        break
        elif letter == "*":
            show_possible_matches(my_word)
        elif warnings>0:
            print ('you have to enter alphbets Oops! That is not a valid letter')
            warnings = warnings -1
            print (f'warnings left {warnings} and word is {my_word} ')
            continue
        else:
            for l in letters_guessed:
                if l == letter.lower():
                    continue_while = True
                    print('letter has already entered try another letter...')
                    break  
            if continue_while:
                continue
            letters_guessed.append(letter.lower())
           # print(letters_guessed)
            if get_guessed_word(secret_word,letters_guessed) == my_word :
                print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}')
                length = length -1
            else:
                print(f'good guess : {get_guessed_word(secret_word,letters_guessed)}')
                my_word = get_guessed_word(secret_word,letters_guessed)
                if is_word_guessed(secret_word, letters_guessed):
                    print('you have won the game')
    if is_word_guessed(secret_word, letters_guessed):
        print('you have won the game')               
    else:
        print(f'you have lost the game try again\n the word is {secret_word}')


    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)

    hangman_with_hints(secret_word)
 

#sudo apt install build-essential dkms linux-headers-$(uname -r)
