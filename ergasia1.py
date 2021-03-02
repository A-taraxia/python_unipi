"""
1.Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει την διάσταση
ενός τετραγώνου και θα φτιάχνει μέσα από λίστες τον αντίστοιχο πίνακα.
Στην συνέχεια θα βρίσκει το πλήθος των θέσεων και θα γεμίζει
στην τύχη τις μισές με μονάδες (στρογγυλοποίηση προς τα πάνω).
Σκοπός είναι να μετρήσετε πόσες τετράδες από μονάδες υπάρχουν
οριζόντια, κάθετα, και διαγώνια. Το πρόγραμμα επαναλαμβάνεται
100 φορές (για την ίδια διάσταση) και επιστρέφει τον μέσο όρο των τετράδων.
"""
import random
import math
fourhor=0
fourver=0
fourdiag=0

col = int(input("δώσε διάσταση τετραγώνου: "))
row = col # ο πινακας ειναι τετραγωνος
for c in range(0,100):
    Square = [[0 for y in range(col)] for x in range(row)] # Master table

    theseis = (col * row)
    half = math.ceil(theseis/2)

    i=0
    while i <  half:
        x = random.randint(0,theseis-1)
        gr = x // row
        st = x % col
        if Square[gr][st] == 0:
            Square[gr][st] = 1
            i+=1


    # Horizontal
    for i in range(0,row):
        temp=0
        for j in range(0,col):
            if Square[i][j] == 1:
                temp+=1
            else:
                temp=0
            if temp==4:
                fourhor=fourhor +1
                temp-=1

    #Vertical
    for j in range(0,col):
        temp=0
        for i in range(0,row):
            if Square[i][j] == 1:
                temp+=1
            else:
                temp=0
            if temp==4:
                fourver=fourver +1
                temp-=1

    #diagonal
    NWdiag=[[] for _  in range(row + col-1) ]
    NEdiag=[[] for _ in range(len(NWdiag)) ]
    max= row - 1
    for j in range(0,col):
     for i in range (0,row):
      NWdiag[i+j].append(Square[i][j])
      NEdiag[i-j+max].append(Square[i][j])
    bhma=0
    for i in range (0,col):
        pl=0
        pl2=0
        bhma+=1
        for j in range(0,bhma):
            if NWdiag[i][j]==1:
                pl+=1
                if pl>3:
                    fourdiag+=1
            else:
                pl=0
            if NEdiag[i][j]==1:
                pl2+=1

                if pl2 > 3:
                    fourdiag+=1
            else:
                pl2=0
    bhma=row
    for i in range ((row),(theseis-1)):
        pl=0
        pl2=0
        bhma=bhma-1
        for j in range(0,bhma):
            if NWdiag[i][j]==1:
                pl+=1
                if pl>3:
                    fourdiag+=1
            else:
                pl=0
            if NEdiag[i][j]==1:
                pl2+=1
                if pl2>3:
                    fourdiag+=1
            else:
                pl2=0
print("ο μεσος ορος τετραδων καθετα ειναι:",fourhor/100 )
print("ο μεσος ορος τετραδων οριζοντια ειναι:",fourver/100)
print("ο μεσος ορος τετραδων στις διαγωνιους ειναι:",fourdiag/100)
