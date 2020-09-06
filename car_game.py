#! python3
checker = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if checker:
            print ("Car is already started!")
        else:
            print ("Car started ...")
            checker = True
    elif command == 'stop':
        if not checker:
            print ("Car is already stopped!")
        else:
            print ("Car stopped.")
            checker = False
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
"""
        )
    elif command == 'quit':
        break
    else:
        print("Sorry, I Don't understand that")