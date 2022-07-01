command = ""
started = False

while(command != "exit"):
    command = input("> ").lower()
    if command == "start" and not started:
        started = True
        print("the car is started...")
    elif command == "start" and started:
        print("The car is started already!!")
    elif command == "stop" and started:
        print("the car is stopped...")
        started = False
    elif command == "stop" and not started:
        print("The car is already Stopped")
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
