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
LETTER_SCORE = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}
def score_word(word):
    word = word.upper()
    point = 0
    for letter in word:
        point += LETTER_SCORE[letter]
    if len(word) >= 7:
        point += 8
    return point

def get_highest_word_score(word_list):

    highest = "" , 0
    for word in word_list:
        score = score_word(word)

        if score > highest[1]:
            highest = word, score        
        elif score == highest[1]:
            if  len(highest[0]) == 10:
                continue
            elif len(word) == 10 or len(highest[0]) > len(word):
                highest = word, score       

    return highest