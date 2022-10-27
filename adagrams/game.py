import random

POOL_LETTERS_DICT = {
                        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
                        'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
                        'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1 }


def create_pool_letters_list(POOL_LETTERS_DICT):
    available_letters_list = list()
    for letter in POOL_LETTERS_DICT:
        for i in range(POOL_LETTERS_DICT[letter]):
            available_letters_list.append(letter)
    return available_letters_list

def draw_letters():
    number_of_letters = 10
    all_letter_list = create_pool_letters_list(POOL_LETTERS_DICT)
    player_letters_list = ['','','','','','','','','','']
    for i in range(number_of_letters):
        random_index = random.randint(0, len(all_letter_list) - 1)
        player_letters_list[i]= all_letter_list.pop(random_index)
    return player_letters_list

def uses_available_letters(word, letter_bank):
    checked_word = list()
    word_list = []
    word_list[:] = word.upper()
    for letter in word_list:
        if letter in letter_bank:
            checked_word.append(letter)
            index = letter_bank.index(letter)
            del letter_bank[index]
            if checked_word == word_list:
                letter_bank.extend(checked_word)
                letter_bank.sort()
                return True
    return False

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass