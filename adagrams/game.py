import random
from collections import Counter
import copy
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
    count = 0
    result = []
    deep_copy_dict = copy.deepcopy(LETTER_POOL)
    #print(result)
    while count < 10:
        letter =  random.choice(list(deep_copy_dict.keys()))
        #print(letter)
        deep_copy_dict[letter] -= 1
        #print(LETTER_POOL[letter])
        result.append(str(letter))

        if deep_copy_dict[letter] == 0:
            deep_copy_dict.pop(letter)
        count += 1
    
    return result






def uses_available_letters(word, letter_bank):
    word = word.upper()
    new_word = "".join(word.split())
    word_counter = Counter(new_word)
    letter_bank_counter = Counter(letter_bank)
    for key, value in word_counter.items():
        if key not in letter_bank:
            return False
        elif key in letter_bank and value <= letter_bank_counter[key]:
            return True
        else:
            return False


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass