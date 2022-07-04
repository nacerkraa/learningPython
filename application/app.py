
import random

class lib:

    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second

libo = lib()

print(libo.roll())