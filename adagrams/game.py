import random
from collections import Counter


def draw_letters():
    letter_pool = "AAAAAAAAABBCCDDDDEEEEEEEEEEEEFFGGGHHIIIIIIIII"\
        "JKLLLLMMNNNNNNOOOOOOOOPPQRRRRRRSSSSTTTTTTUUUUVVWWXYYZ"
    letter_counter = Counter(letter_pool)
    letters_draw = []

    count = 10
    while count != 0:
        letter = random.choice(letter_pool)
        if letter_counter[letter] != 0:
            letters_draw.append(letter)
            letter_counter[letter] -= 1
            count -= 1
    return letters_draw


def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_bank_counter = Counter(letter_bank)
    word_counter = Counter(word)
    for key in word_counter:
        if key not in letter_bank_counter:
            return False
        if word_counter[key] > letter_bank_counter[key]:
            return False
    return True


def score_word(word):
    word = word.upper()
    length = len(word)
    if length in [7, 8, 9, 10]:
        score = 8
    else:
        score = 0

    for ch in word:
        if ch in ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]:
            score += 1
        elif ch in ["D", "G"]:
            score += 2
        elif ch in ["B", "C", "M", "P"]:
            score += 3
        elif ch in ["F", "H", "V", "W", "Y"]:
            score += 4
        elif ch == "K":
            score += 5
        elif ch in ["J", "X"]:
            score += 8
        else:
            score += 10
    return score


def get_highest_word_score(word_list):
    result = [word_list[0], score_word(word_list[0])]

    for i in range(1, len(word_list)):
        curr_score = score_word(word_list[i])
        if curr_score > result[1]:
            result[0] = word_list[i]
            result[1] = curr_score
        elif curr_score == result[1]:
            if len(result[0]) < 10 and len(word_list[i]) == 10:
                result[0] = word_list[i]
                result[1] = curr_score
            elif len(word_list[i]) < len(result[0]) and len(result[0]) != 10:
                result[0] = word_list[i]
                result[1] = curr_score

    return tuple(result)
