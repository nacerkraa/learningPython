# Define a function

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid Value")