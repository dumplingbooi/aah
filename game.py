import random 

repeat = True

while repeat:
    number = random.randint(1, 100)
    guess = 0
    tries = 0

    while guess != number:
        if guess < number:
            print ("Pameiģini lielāku skaitli")
        else:
            print ("Pameiģini mazāku skaitli")

        guess = int(input("Uzmini skaitli: "))
        tries += 1
    else:
        if tries < 3:
            print(F" woah, gadalka Tu uzminēji pēc {tries} reizēm")
        elif tries < 6:
            print(F" not bad, Tu uzminēji pēc {tries} reizēm")
        else:
            print(F" bots, Tu uzminēji pēc {tries} reizēm")

    response = input("Vai gribi turpināt y/n: ")
    if response == "y":
        repeat = True
    elif response == "n":
        repeat = False
        print("Paldies par spēli! bye, bye")
    else:
        repeat = False
        print("Paldies par spēli! bye, bye")
