#GAME "GUESS A NUMBER"

import random
print("The game begins")
print("The game is over when Α) the number is found Β) by pressing enter")
total_points=0
while True:
    random_number=random.randint(1,100)
    tries=0
    while True:
        try_number=input("Guess number:(1-100)")
        if try_number=="":
            print("Game over")
            break
        if not try_number.isdigit():continue
        try_number=int(try_number)
        if try_number<1 or try_number>100:continue
        tries+=1
        if try_number==random_number:
            if tries>=10:
                points=0
            else:
                points=10-tries
            print("You found it after {} tries, and you earned {} points".format(tries,points))
            total_points+=points
            reply=""
            while reply!="YES" and reply!="NO":
                reply=input("Wanna play again?(YES/NO)")
            if reply=="YES":break
            elif reply=="NO":
                print("You earned {} points\nΚαλή συνέχεια".format(total_points))
                break
        elif try_number<random_number:print("The hidden number is bigger ")
        else:print("Τhe hidden number is lower ")
    if try_number=="" or reply=="NO":break
