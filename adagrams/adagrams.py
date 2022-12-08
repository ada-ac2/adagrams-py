from adagrams.player import Player

class Adagrams():
    def __init__(self, letter_pool, letter_values) -> None:
        self.letter_pool = letter_pool
        self.letter_values = letter_values
        self.player = Player(letter_pool)
        self.words = []

    def score_word(self, word):
        score = 0
        for letter in word:
            score += self.letter_values[letter.upper()]

        if len(word) > 6 and len(word) < 11:
            score += 8

        return score