#! python3
numbers = [12, 15, 1, 2, 17, 21, 15]
checker = numbers[0]
for number in numbers:
    if number > checker:
        checker = number
print(checker)