def affiche(n1, n2):
    for i in range(n1, n2+1):
        if i % 3 == 0 and i % 5 == 0:
            print("Frisbee", end="")
        elif i % 3 == 0:
            print("Fizz", end="")
        elif i % 5 == 0:
            print("Buzz", end="")
        else:
            print(i, end="")
affiche(5, 10)
#affiche(10, 16)


