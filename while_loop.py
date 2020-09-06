#! python3
 
i = 1
while i < 4:
    number = int(input("Guess: "))
    i = i + 1
    if number == 9:
        print('You win!')
        break
else:
        print('You lose!')
 