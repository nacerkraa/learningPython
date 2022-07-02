# Define A Dictionnary

message = input("> ")
words = message.split(" ")
emojes = {
    ":)": "🙂",
    ":(": "🙁",
}

output = ""

for word in words:
    output += emojes.get(word, word) + " "

print(output)