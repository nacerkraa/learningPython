# Define A Dictionnary


dic = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}

number = input("number: ")

output = ""
for ch in number:
    output += dic.get(ch,"?") + " "

print(output)