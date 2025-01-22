from random import randrange
import time

z = 0
x = 0
ready = False
print("Právě teď máte",x, "bodů.")
odpoved = input("Přejete si otočit kartu? Zadejte y/n \n")
while odpoved not in ["y", "n"]:
        print("\nZadejte prosím pouze 'n' či 'y' \n")
        odpoved = input("Přejete si otočit kartu? Zadejte y/n \n")
while odpoved == "y":
    n = randrange(2,10)
    x = x + n
    time.sleep(1)
    print("\nKarta obrací číslo", n)
    if x > 21:
        print("Prohrál jste! Váš počet bodů je", x)
        break
    if x == 21:
        ready = True
        print("Výborně! Právě teď máte",x, "bodů.")
        time.sleep(1)
        break
    print("Dohromady máte", x, "bodů.\n")
    time.sleep(1)
    odpoved = input("Přejete si otočit kartu? Zadejte y/n \n")
    while odpoved not in ["y", "n"]:
        print("\nZadejte prosím pouze 'n' či 'y' \n")
        odpoved = input("Přejete si otočit kartu? Zadejte y/n \n")
        print("Zadejte prosím pouze 'n' či 'y' \n")
        odpoved = input("Přejete si otočit kartu? Zadejte y/n \n")
    if odpoved == "n":
        ready = True
if ready:
    print("Nyní karty vykládá dealer...\n")
    time.sleep(2)
    while z <= x or z == 0:
        print("Dealer si bere kartu...")
        time.sleep(1)
        g = randrange(2,10)
        z = z + g
        print("Dealer vytáhl", g, "! " "(",z,")\n")
        if z <= 21 and z > x:
            print("Prohrál jste.") 
            break   
        if z == 21 and x == 21:
            print ("Remíza!")
            break
        if z > 21:
            print ("Vyhrál jste!")


