command = ""

while(command != "exit"):
    command = input("> ").lower()
    if command == "start":
        print("the car is started...")
    elif command == "stoped":
        print("the car is stopped...")
    elif command == "help":
        print('''
            start- the car is started
            stop- the car is stop the car
            exit- for quit the car
        ''')
    elif command == "exit":
        print("quit the cmd")
        break
    else:
        print("Error: Please Write A Valid Command")
