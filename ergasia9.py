"""
Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII
κειμένου και μετατρέπει τον κάθε χαρακτήρα στον αντίστοιχο αριθμό ASCII και
κρατάει τους μονούς. Εμφανίστε τα στατιστικά εμφάνισης του κάθε γράμματος με
“μπάρες” χρησιμοποιώντας το χαρακτήρα *, όπου κάθε * αντιστοιχεί σε 1%.
Η στρογγυλοποίηση θα γίνει προς τα πάνω.
"""

# Γράψτε ένα κώδικα σε Python ο οποίος
# να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου και
import math

file_to_open = input("Δώσε αρχείο:")
try:
    file = open(file_to_open, "r")
except FileNotFoundError:
    print("Το αρχειό δεν υπάρχει. Προσπαθήστε ξανά.")
    exit(1)

# μετατρέπει τον κάθε χαρακτήρα στον αντίστοιχο αριθμό ASCII και
# κρατάει τους μονούς.
count = {}
for line in file:
    for character in line:
        if ord(character) % 2 != 0:  # if number is odd
            if character in count:
                count[character] += 1  # add character to dictionary
            else:
                count[character] = 1  # first occurrence of character
file.close()

# Εμφανίστε τα στατιστικά εμφάνισης του κάθε γράμματος με “μπάρες” χρησιμοποιώντας το χαρακτήρα *,
# όπου κάθε * αντιστοιχεί σε 1%

odd_chars = 0
for key in count:
    odd_chars += count[key]  # calculate total amount of odd characters

stats = count.copy()  # create copy of count dictionary
for key in count:
    x = count[key] / odd_chars * 100  # calculate percentage
    stats[key] = math.ceil(x)  # replace each value with percentage (round up)

star_char = '*'
for key in stats:
    print(key, ':', stats[key] * star_char)  # print bar
