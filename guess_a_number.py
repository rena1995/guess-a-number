#ΠΑΙΧΝΙΔΙ "ΜΑΝΤΕΨΕ ΕΝΑ ΑΡΙΘΜΟ"

import random
print("Το παιχνίδι αρχίζει")
print("Το παιχνίδι τερματίζει Α) με την εύρεση του αριθμού Β) πατώντας enter")
total_points=0
while True:
    random_number=random.randint(1,100)
    tries=0
    while True:
        try_number=input("Μάντεψε αριθμό:(1-100)")
        if try_number=="":
            print("Τερματισμός παιχνιδιού")
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
            print("Το βρήκατε μετά από {} προσπάθειες, και κερδίσατε {} πόντους".format(tries,points))
            total_points+=points
            reply=""
            while reply!="ΝΑΙ" and reply!="ΟΧΙ":
                reply=input("Να ξαναπαίξουμε;(ΝΑΙ/ΟΧΙ)")
            if reply=="ΝΑΙ":break
            elif reply=="ΟΧΙ":
                print("Κέρδισες {} πόντους\nΚαλή συνέχεια".format(total_points))
                break
        elif try_number<random_number:print("Ο κρυμμένος αριθμός είναι μεγαλύτερος ")
        else:print("Ο κρυμμένος αριθμός είναι μικρότερος ")
    if try_number=="" or reply=="ΟΧΙ":break
