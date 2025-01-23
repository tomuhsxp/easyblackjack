import random
import time

z = 0
x = 0
mylist = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]
ready = False
print("You currently have",x, "points.")
answer = input("Do you wish to take a card? Type 'y'/'n' \n")
while answer not in ["y", "n"]:
        print("\nUnknown input. Please type ONLY 'y' or 'n' \n")
        answer = input("Do you wish to take a card? Type 'y'/'n' \n")
while answer == "y":
    n = random.choice(mylist)
    mylist.remove(n)
    x = x + n
    time.sleep(1)
    print("\nYour card is a", n)
    if x > 21:
        print("You lost! With", x, "points.")
        break
    if x == 21:
        ready = True
        print("Excellent! You now have", x, "points.")
        time.sleep(1)
        break
    print("You currently have", x, "points.\n")
    time.sleep(1)
    answer = input("Do you wish to take a card? Type 'y'/'n' \n")
    while answer not in ["y", "n"]:
        print("\nUnknown input. Please type ONLY 'y' or 'n' \n")
        answer = input("Do you wish to take a card? Type 'y'/'n' \n")
        print("Unknown input. Please type ONLY 'y' or 'n' \n")
        answer = input("Do you wish to take a card? Type 'y'/'n' \n")
    if answer == "n":
        ready = True
if ready:
    print("The dealer is now playing...\n")
    time.sleep(2)
    while z <= x or z == 0:
        print("Dealer picks a card...")
        time.sleep(1)
        g = random.choice(mylist)
        mylist.remove(g)
        z = z + g
        print("Dealer got", g, "! " "(",z,")\n")
        if z <= 21 and z > x:
            print("You lost.") 
            break   
        if z == 21 and x == 21:
            print ("Draw!")
            break
        if z > 21:
            print ("You won!")


