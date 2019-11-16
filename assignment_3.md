Για τις επόμενες ασκήσεις θα πρέπει να κατεβάσετε το αρχείο που βρίσκετε στο εξής link: https://raw.githubusercontent.com/washingtonpost/data-game-of-thrones-deaths/master/game-of-thrones-deaths-data.csv 

Ένας τρόπος για να το κατεβάσετε είναι το τρέξετε την εντολή:

```bash
wget https://raw.githubusercontent.com/washingtonpost/data-game-of-thrones-deaths/master/game-of-thrones-deaths-data.csv  
```

Αυτό το αρχείο είναι σε μορφή [csv](https://en.wikipedia.org/wiki/Comma-separated_values). 
Περιέχει όλους τους.. θανάτους που έγιναν στο (Game of Thrones)(https://www.imdb.com/title/tt0944947/). 
Περισσότερα για το αρχείο αυτό μπορείτε να διαβάσετε [εδώ](https://github.com/washingtonpost/data-game-of-thrones-deaths) και [εδώ](https://www.washingtonpost.com/graphics/entertainment/game-of-thrones/) υπάρχει μία φανταστική παρουσίασή του.

Η πρώτη γραμμή του αρχείου περιέχει την επικεφαλίδα (header) με τα εξής πεδία:
order,season,episode,character_killed,killer,method,method_cat,reason,location,allegiance,importance
* order: Η σειρά με την εοποία έγινε ο θάνατος
* season: H σεζόν
* episdose: Το επεισόδιο της σεζόν
* character_killed: Ποιος πέθανε
* killer: Ποιος τον σκότωσε
* method: Με ποιον τρόπο τον σκότωσε
* method_cat: Η κατηγορία του τρόπου που τον σκότωσε
* reason: Ο λόγος για τον οποίο τον σκότωσε
* location: Ο τόπος που σκοτώθηκε
* allegiance: Σε ποια φατρία/οικογένεια/φυλή ανοίκει αυτός που πέθανε
* importance: Ένας αριθμός από το 1 μέχρι το 4. Υποδηλώνει πόσο σημαντικό για την πλοκή είναι ο θάνατος. 1=ασήμαντος, 4=πολύ σημαντικός.

Δίνεται επίσης ο εξής κώδικας για να αποθηκεύσετε όλα τα δεδομένα σε μία λίστα:

```python
import csv

order_index = 0
season_index = 1
episode_index = 2
character_killed_index = 3
killer_index = 4
method_index = 5
method_cat_index = 6
reason_index = 7
location_index = 8
allegiance_index = 9
importance_index = 10

data = []
with open('game-of-thrones-deaths-data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    header = f.readline().strip().split(',')
    for ls in reader:
        d = {
            'order': int(ls[order_index]),
            'season': int(ls[season_index]),
            'episode': int(ls[episode_index]),
            'character_killed': ls[character_killed_index],
            'killer': ls[killer_index],
            'method': ls[method_index],
            'method_cat': ls[method_cat_index],
            'reason': ls[reason_index],
            'location': ls[location_index],
            'allegiance': ls[allegiance_index],
            'importance': int(ls[importance_index]) if ls[importance_index] else 1,
        }
        data.append(d)
```

Κάθε στοιχείο της λίστας έχει ένα dictionary με όλα τα πεδία. 

Εσείς θα πρέπει να γράψετε κώδικα που να απαντάει στα εξής ερωτήματα (εννοείται ότι δεν χρειάζεται να έχετε παρακολουθήσει τη σειρά για να απαντήσετε): 

###  Άσκηση 1
Πόσοι θάνατοι έχουν importance μεγαλύτερο από 1;

### Άσκηση 2
Από όσους έχουν importance μεγαλύτερο από 1, πόσοι έχουν σκοτωθεί από την Arya Stark;

### Άσκηση 3
Σε ποια σεζόν έχει σκοτώσει περισσότερους ο Jon Snow; Πάρτε μόνο όσους έχουν importance μεγαλύτερο από 1.

### Άσκηση 4
Πόσες διαφορετικές κατηγορίες θανάτου (method_cat) υπάρχουν;

### Άσκηση 5
Για κάθε διαφορετική κατηγορία θανάτου, σε ποιά φατρία/οικογένεια/φυλή ανοίκουν τα μέλη που έχουν σκοτωθεί τις περισσότερες φορές από αυτή τη κατηγορία; Πάρτε μόνο θανάτους με importance>1

### Άσκηση 6
Ποιος έχει κάνει τους 2ους περισσότερους φόνους με importance>1;

### Άσκηση 7
Ποιος είναι ο λόγος (reason) που προκάλεσε τους περισσότερους θανάτους με importance>2;

### Άσκηση 8
Σε ποια επεισόδια δεν έγινε κανένας θάνατος; (τυπώστε και τη σεζόν του κάθε επεισοδίου)

### Άσκηση 9
Αν πάρουμε όλα τα διαφορετικά ζευγάρια (θύτης,θύμα) και όλα τα διαφορεικά ζευγάρια (θύμα,θήτης), πόσα κοινά στοιχεία υπάρχουν μεταξύ τους;

### Άσκηση 10
Πόσος είναι ο μέσος όρος θανάτων ανά επεισόδια για κάθε σεζόν; Δηλαδή για κάθε σεζόν (8 συνολικά), τυπώστε τον μέσο όρο από θανάτους που είχε το κάθε επεισόδιο αυτής της σεζόν. 

### Άσκηση 11 (εξαιρετικά δύσκολη)
Ας υποθέσουμε ότι έχουμε μία σειρά από φόνους: ο Α σκοτώνεται από τον Β, ο Β σκοτώνεται από τον Γ και τέλος ο Γ σκοτώνεται από τον Δ. Έχουμε δηλαδή μία σειρά από 4 φόνους όπου ο ν-οστός σκοτώνεται από το (ν+1)-στο. Ποια είναι η μεγαλύτερη αλυσίδα από φόνους που βλέπουμε στο games of thrones;

Hint: Στην ουσία ζητάμε να βρούμε τη μεγαλύτερη διαδρομή σε έναν γράφο όπου κόμβοι είναι χαρακτήρες και ακμές είναι.. φόνοι. Μπορείτε να προσαρμόσετε τον κώδικα που υπάρχει εδώ: https://stackoverflow.com/questions/29320556/finding-longest-path-in-a-graph 
















