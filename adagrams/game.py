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
        elif key in letter_bank :
            if value <= letter_bank_counter[key]:
                continue
            else:
                return False

    return True

Score_chart = {
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
def score_word(word):
    score = 0
    word = word.upper()
    new_word = "".join(word.split())
    for cha in new_word:
        score += Score_chart[cha]
    if 7 <= len(new_word) <= 10:
        score += 8
    return score

def get_highest_word_score(word_list):
    word_score_dict = {}
    for word in word_list:
        score = score_word(word)
        if score not in word_score_dict.keys():
            word_score_dict[score] = [word]
        else:
            word_score_dict[score].append(word)
   
    highest_scores = max(word_score_dict.keys())
    
    highest_score_word_lst = word_score_dict[highest_scores]
    len_lst = []
    result = []
    for word in highest_score_word_lst:
        len_lst.append(len(word))
    print(f"len_lst, {len_lst}")
    if 10 in len_lst:
        result.append(highest_score_word_lst[len_lst.index(10)])
        result.append(highest_scores)
        return tuple(result)
    else:    
        min_1 = min(len_lst)
        min_index = len_lst.index(min_1)
        print(highest_score_word_lst[min_index])
        result.append(highest_score_word_lst[min_index])
        result.append(highest_scores)
        return tuple(result)
        
    
    

        
        
    
   