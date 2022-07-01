command = ""
is_started = False

while(command != "exit"):
    command = input("> ").lower()
    if command == "start" and is_started == False:
        is_started = True
        print("the car is started...")
    elif command == "start" and is_started == True:
        print("The car is started already!!")
    elif command == "stop" and is_started == True:
        print("the car is stopped...")
        is_started = False
    elif command == "stop" and is_started == False:
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
