# Define a function

try:
    age = int(input("Age: "))
    print(age)
    age2 = age / 0
except ZeroDivisionError:
    print("Age can not divise by Zero!")
except ValueError:
    print("Invalid!")