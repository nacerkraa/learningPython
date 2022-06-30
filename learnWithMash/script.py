from email import message


secrit = 9
i = 1
message = "You field!"

while(i <= 3): 
    guess = int(input("Guess: "))
    if(guess == secrit):
        message = "you win!"
        break
    i += 1

print(message)
