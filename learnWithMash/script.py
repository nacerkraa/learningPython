
from os import remove



numberes = [6, 3, 1, 6, 5, 3]
uniques = []


for item in numberes:
    if item not in uniques:
        uniques.append(item)

print(uniques)