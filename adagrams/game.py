import random 

#constants
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


def draw_letters():
    letter_freq_array = []
    drawn_letters = []
    
    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
            letter_freq_array.append(letter)

    for i in range(10):
        random_letter = random.choice(letter_freq_array) 
        letter_freq_array.remove(random_letter)
        drawn_letters.append(random_letter)
    return drawn_letters


def uses_available_letters(word, letter_bank):
    letters_from_word = list(word.upper())
    for letter in letters_from_word:
        if letter in letter_bank:
            letters_from_word_freq = letters_from_word.count(letter)
            letters_from_bank_freq = letter_bank.count(letter)
            if letters_from_word_freq > letters_from_bank_freq:
                return False
        else:
            return False
    return True

def score_word(word):
    letters_from_word = list(word.upper())
    score = 0.0
    for letter in letters_from_word:
        score += SCORE_CHART[letter]
    if len(word) >=7:
        score+= 8
    return score

def get_highest_word_score(word_list):
    highest_word_score = "", 0

    for word in word_list:
        score = score_word(word) 
        if score > highest_word_score[1]:
            highest_word_score = word, score
        elif score == highest_word_score[1]:
            if len(word) != len(highest_word_score[0]):
                if len(word) == 10:
                    highest_word_score = word, score
                elif len(word) < len(highest_word_score[0]):
                    if len(highest_word_score[0]) != 10:
                        highest_word_score = word, score
                                
    return highest_word_score


