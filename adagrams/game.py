import random

def draw_letters():
    letters =  ["a", "s", "m", "l", "q", "k", "e", "o", "w", "d", "e"]
    random.shuffle(letters)
    # important to do this twice!
    random.shuffle(letters)
    
    return letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass