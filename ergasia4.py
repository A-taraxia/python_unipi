"""
Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει
σαν είσοδο ένα αρχείο ASCII κειμένου και να το
κόβει σε συνεχόμενες τριάδες λέξεων(όλες τις δυνατές).
Στην συνέχεια,διαλέγει τυχαία μια τριάδα και προσπαθεί
να συντάξει ένα τυχαίο κείμενο από αυτό,
χρησιμοποιώντας τις δυο τελευταίες λέξεις και επιλέγοντας
μια τριάδα που να ξεκινάει από αυτές τις δυο.
Το πρόγραμμα ολοκληρώνεται, όταν γράψει 200 λέξεις ή δεν
μπορεί να επιλεγχεί άλλη τριάδα λέξεων.
"""
import math
import random
#άνοιγμα του αρχείου ascii
try:
    file = open(input("Δώσε αρχείο:"), "r")
except FileNotFoundError:
    print("Το αρχειό δεν υπάρχει. Προσπαθήστε ξανά.")
    exit(1)
#μετατροπή file σε string
string = file.read().replace("\n", " ")
file.close()
words = string.split()
grouped_words = [' '.join(words[i: i + 3]) for i in range(0, len(words), 3)]
tot_words=len(words)#amount of words in text
tot_three=math.floor(tot_words/3)#amount of groups of tot_three

#construction of new random text
if tot_words>200:
    x=random.sample(range(tot_three),(math.ceil(200/3)))
else:
    x=random.sample(range(tot_three),tot_three)
new=''
for i in range(0,len(x)-1):
    new+=" "+grouped_words[x[i]]
print(new)
