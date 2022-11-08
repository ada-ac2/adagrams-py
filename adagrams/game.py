import random
from collections import Counter
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
    #print(result)
    while count < 10:
        letter =  random.choice(list(LETTER_POOL.keys()))
        #print(letter)
        LETTER_POOL[letter] -= 1
        #print(LETTER_POOL[letter])
        result.append(str(letter))

        if LETTER_POOL[letter] == 0:
            LETTER_POOL.pop(letter)
        count += 1
    return result






def uses_available_letters(word, letter_bank):
    word = word.upper()
    #word_dict = {}
    print(word)
    print(letter_bank)
    new_word = "".join(word.split())

    print(new_word)
    d = Counter(new_word)
    e = Counter(letter_bank)
    print(d)



    for key, value in d.items():
        if key not in letter_bank:
            return False
        elif key in letter_bank and value <= e[key]:
            return True
        else:
            return False






    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass