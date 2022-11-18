import string
import random
def draw_letters():
    letters_dictionary = {
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

    letters_drawn_in_hand = []
    letter_count = 0
    while letter_count < 10:
            letter_chosen = (random.choice(string.ascii_letters))
            letter_chosen = letter_chosen.capitalize()

            if letters_dictionary[letter_chosen] > 0:
                letters_drawn_in_hand.append(letter_chosen)
                letter_count += 1
                letters_dictionary[letter_chosen] -= 1
    return letters_drawn_in_hand

def uses_available_letters(word, letter_bank):
    uppercase_word = word.upper()
    selected_letters = letter_bank.copy()

    for each_char in uppercase_word:
        try:
            selected_letters.remove(each_char)
        except ValueError:
            return False
    return True

def score_word(word):
    dict_for_letter_points = {("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1, 
    ("D", "G"): 2, 
    ("B", "C", "M", "P"): 3, ("F", "H", "V", "W", "Y"): 4,
    ("K"): 5, ("J", "X"): 8, ("Q", "Z"): 10}
    points_for_the_word = 0
    uppercase_word = word.upper()
    for each_char in uppercase_word:
        for each_key_in_dict in dict_for_letter_points.keys():
            if each_char in each_key_in_dict:
                points_for_the_word += dict_for_letter_points[each_key_in_dict]
    if len(word) >= 7:
        points_for_the_word += 8

    return points_for_the_word


def get_highest_word_score(word_list):
    words_score_dict = {}
    max_score_sofar = -1
    for each_word in word_list:
        score_of_this_word = score_word(each_word)
        words_score_dict[each_word] = score_of_this_word
        if score_of_this_word > max_score_sofar:
            max_score_sofar = score_of_this_word
    winning_word_with_max_score = ()
    lowest_word_length = 11
    for each_word, word_score in words_score_dict.items():
        if word_score == max_score_sofar:
            if len(each_word) == 10:
                winning_word_with_max_score = (each_word ,word_score)
                break
            if len(each_word) < lowest_word_length:
                lowest_word_length = len(each_word)
                winning_word_with_max_score = (each_word ,word_score)
    return winning_word_with_max_score