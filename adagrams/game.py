import random
from collections import defaultdict

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
    letters = LETTER_POOL.keys()
    counts = LETTER_POOL.values()
    available_letters = random.sample(letters, counts=counts, k=10)
    return available_letters


def uses_available_letters(word, letter_bank): 
    available_letters = defaultdict(int)
    for letter in letter_bank:
        available_letters[letter] += 1
    
    for character in word:
        character = character.upper() # ignore case difference
        if character not in available_letters or available_letters[character] == 0:
            return False
        available_letters[character] -= 1
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass