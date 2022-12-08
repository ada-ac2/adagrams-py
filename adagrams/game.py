import copy
import random

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

LETTER_VALUES = {
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
    'P': 2, 
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

def draw_letters():
    letter_pool_copy = copy.deepcopy(LETTER_POOL)
    letters = []

    while len(letters) < 10:
        letter = random.choice(list(letter_pool_copy.keys()))
        if letter_pool_copy[letter] > 0:
            letters.append(letter)
            letter_pool_copy[letter] -= 1

    return letters

def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.deepcopy(letter_bank)
    word = word.upper()

    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    
    return True

def score_word(word):
    score = 0
    for letter in word:
        score += LETTER_VALUES[letter.upper()]

    if len(word) > 6 and len(word) < 11:
        score += 8

    return score

def get_highest_word_score(word_list):
    highest = (word_list[0],0)
    for word in word_list:
        score = score_word(word)
        if score > highest[1]:
            highest = (word, score)
        elif score == highest[1]:
            if len(highest[0]) == 10:
                pass
            elif len(word) == 10 and len(highest[0]) != 10:
                highest = (word, score)
            elif len(word) < len(highest[0]):
                highest = (word, score)

    return highest