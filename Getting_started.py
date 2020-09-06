#! python3
name = input("What is your name?")

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be maximumm of 50 characters")
else: print("name looks good")