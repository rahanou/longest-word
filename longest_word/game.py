import random
import string

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)] # TODO


    def is_valid(self, word: str) -> bool:
        if len(word)==0:
            return False

        for letter in word:
            if letter not in self.grid:
                return False
            else:
                return True
