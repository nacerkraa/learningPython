

def find_max(NumberList):
    max = NumberList[0]

    for number in NumberList:
        if number > max:
            max = number
    print(max)