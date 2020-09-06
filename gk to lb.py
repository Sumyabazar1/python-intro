#! python3
weight = input("Weight: ")
weight = int(weight)
if (weight > 0 ):
    define = input("(L)bs or (K)g: ")
    if define.upper() == "L":
        weight = weight * 0.45
        print(f"you are {weight} kilos")
    elif (define.upper() == 'K'):
        weight = weight * 2.20
        print(f"you are {weight} pounds")