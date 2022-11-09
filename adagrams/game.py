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

def draw_letters():
    #array representing frequency of letters
    letter_freq_array = []
    #array representing drawn letters
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
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass