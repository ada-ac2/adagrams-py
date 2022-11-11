import random
from copy import deepcopy
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    letter_pool = deepcopy(LETTER_POOL)
    letters = []
    i = 10
    while i > 0:
        key = chr(random.randint(0, 25)+ 65)
        if letter_pool[key] != 0:
            letters.append(key)
            letter_pool[key] -= 1
            i -= 1
        else:
            continue      
    return letters

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_freq = {}
    for letter in letter_bank:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1
    for letter in word:
        if letter not in letter_freq:
            return False
        elif letter_freq[letter] > 0:
            letter_freq[letter] -= 1
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass