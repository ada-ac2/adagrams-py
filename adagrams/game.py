import random

# Dictionary of letters and available number of duplicates of each letter
POOL_LETTERS_DICT = {
                        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
                        'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
                        'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1 }

# Dictionary of letters and points it give to the user. keys: points, values: lists of letters
SCORE_CHART = {
                1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
                2: ['D', 'G'],
                3: ['B', 'C', 'M', 'P'],
                4: ['F', 'H', 'V', 'W', 'Y'],
                5: ['K'],
                8: ['J', 'X'],
                10: ['Q', 'Z'] 
}


def create_pool_letters_list(POOL_LETTERS_DICT):
    '''
    This function convert POOL_LETTERS_DICT into the available_letters_list;
    has parameter = POOL_LETTERS_DICT;
    Returns available_letters_list which contain letters duplicates as shown in value of the key(letter) in dictionary
    '''  
    available_letters_list = list()
    for letter in POOL_LETTERS_DICT:
        for i in range(POOL_LETTERS_DICT[letter]):
            available_letters_list.append(letter)
    return available_letters_list

def draw_letters():
    '''
    This function has no parameters;
    Returns an array of ten strings (each one letter which randomly drawn from available_letters_list
    '''    
    number_of_letters = 10
    all_letter_list = create_pool_letters_list(POOL_LETTERS_DICT)
    player_letters_list = ['','','','','','','','','','']
    for i in range(number_of_letters):
        random_index = random.randint(0, len(all_letter_list) - 1)
        player_letters_list[i]= all_letter_list.pop(random_index)
    return player_letters_list

def uses_available_letters(word, letter_bank):
    '''
    This function has two parameters: input word (string) letter_bank (array of drawn letters from draw_letters function)
    Returns True if every letter in the input word is in the letter_bank
    Returns False if there is a letter in input that is not present in the letter_bank or has too much of compared to the letter_bank
    '''
    checked_word = list()
    word_ls = []
    word_ls[:] = word.upper()
    for letter in word_ls:
        if letter in letter_bank:
            checked_word.append(letter)
            index = letter_bank.index(letter)
            del letter_bank[index]
            if checked_word == word_ls:
                letter_bank.extend(checked_word)
                letter_bank.sort()
                return True
    return False

def score_word(word):
    '''
    This function has one parameter: word, which is a string of characters
    Returns an integer representing the number of points
    Each letter within word has a point value (located in SCORE_CHART dictionary)
    If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points
    '''
    user_points = 0
    word_ls = []
    word_ls[:] = word.upper()
    if len(word_ls)>= 7:
        user_points = 8
    for element in SCORE_CHART:
        for letter in word_ls:
            if letter in SCORE_CHART[element]:
                user_points += element
    return user_points

def get_highest_word_score(word_list):
    '''
    This function has one parameter - word_list( list of strings)
    Returns a tuple that represents the data of a winning word and it's score.
    In the case of tie in scores:
        1 - the word which has 10 letters
        2 - prefer the word with the fewest letters
        3 - the first one in the supplied list
    '''
    users_score = 0
    max_score = 0
    max_word = ''
    for word in word_list:
        users_score = score_word(word)
        if users_score > max_score:
            max_score = users_score
            max_word = word
        elif users_score == max_score:
            if len(word) < len(max_word):
                if len(max_word) == 10:
                    continue
                else:
                    max_score = users_score
                    max_word = word
            elif len(word) == len(max_word):
                word_index = word_list.index(word)
                max_word_index = word_list.index(max_word)
                if word_index > max_word_index:
                    continue
                else:
                    max_word = word
                    max_score = users_score
            elif len(word) == 10:
                max_word = word
                max_score = users_score
    best_word = (max_word, max_score)
    return best_word  # tuple of winning word and it's scores  best_word[ 0 - word , 1 - it's score]