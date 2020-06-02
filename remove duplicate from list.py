#! python3
numbers = [1, 2, 3, 3, 12, 52, 52, 11, 12,]
uniques = []
for dupli in numbers:
    if dupli not in uniques:
        uniques.append(dupli)
print(uniques)