

def find_max(NumberList):
    max = NumberList[0]

    for number in NumberList:
        if number > max:
            max = number
    print(max)

def second_max_number(NumberList):
    NumberList.sort()
    print(NumberList[-2])