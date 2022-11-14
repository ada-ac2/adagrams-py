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

SCORE_CHART = {
    "A":1, "E":1, "I":1, "O":1, "U":1,"L":1, "N":1, "R":1, "S":1, "T":1, "D":2, "G":2, "B":3,
    "C":3, "M":3, "P":3, "F":4, "H":4, "V":4, "W":4, "Y":4, "K":5, "J":8, "X":8, "Q":10, "Z":10
}

def draw_letters():
    letters = list(LETTER_POOL.keys())
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
    total_score = 0
    if len(word) >= 7:
        total_score += 8
    for character in word:
        character = character.upper() # ignore case difference
        indiviual_score = SCORE_CHART[character]
        total_score +=  indiviual_score
    return total_score

def get_highest_word_score(word_list):
    # Check the score in the word_list one by one.
    # If new score is higher or score is the same with current highest score:
    #  - if current word's length is 10 or length is same as new word, keep original one
    #  - if current word's length is longer than the new word or new word's length is 10, take the new word
    cur_score = 0
    cur_word = ""
    for word in word_list:
        score = score_word(word)
        if score > cur_score:
            cur_score = score
            cur_word = word
        elif score == cur_score:  
            cur_length = len(cur_word)  
            if cur_length != 10:   # exception: need to keep the length 10 word.
                if len(word) < cur_length or len(word) == 10: 
                    cur_word = word
    return cur_word, cur_score


