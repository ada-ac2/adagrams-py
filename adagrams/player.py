import copy
import random

class Player:
    def __init__(self, letter_pool):
        self.tiles = self.draw_letters(letter_pool)

    def draw_letters(self, letter_pool):
        letter_pool_copy = copy.deepcopy(letter_pool)
        letters = []

        while len(letters) < 10:
            letter = random.choice(list(letter_pool_copy.keys()))
            if letter_pool_copy[letter] > 0:
                letters.append(letter)
                letter_pool_copy[letter] -= 1

        return letters

    def uses_available_letters(self, word):
        letter_bank_copy = copy.deepcopy(self.tiles)
        word = word.upper()

        for letter in word:
            if letter in letter_bank_copy:
                letter_bank_copy.remove(letter)
            else:
                return False
        
        return True

    def __str__(self) -> str:
        return f"Player's hand contains: {self.tiles}"