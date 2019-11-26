
## Μέρος 1ο. Regular expressions

### Άσκηση 1

Γράψτε **ένα** regular expression το οποίο θα εξάγει όλα τα κομμάτια του κειμένου τα οποία βρίσκονται μεταξύ δύο αριθμών.  
Για παράδειγμα:

```
228djj21  --> ['djj']
421   a  d dd8 --> ['   a  d dd']
abcdefg --> []
fdsd2342dfdf --> []
abcd123defg456kkk777 --> [defg, kkk]
```

### Άσκηση 2
Γράψτε **ένα** regular expression το οποίο θα μπορεί να εντοπίζει ελληνικά κινητά τηλέφωνα. Θα πρέπει να εντοπίζει μέσα σε ένα κείμενο τηλέφωνα όπως:

```
6912345678
00306912345678
+306912345678
```
ΔΕΝ θα πρέπει να εντοπίζει τηλέφωνα όπως:

```
691234567 # Δεν έχει 10 ψηφία
7912345678 # Δεν αρχίζει από 69
+316912345678 # Ο διεθνής κωδικός της Ελλάδας δεν είναι το +31 (είναι το +30)
00316912345678 # Ο διεθνής κωδικός της Ελλάδας δεν είναι το +31 (είναι το +30)
```

### Άσκηση 3
Ο αριθμός [ΑΜΚΑ]((https://www.amka.gr/tieinai.html) αποτελείται από έντεκα (11) αριθμούς και αναλύεται ως κάτωθι:
* Πχ ΑΜΚΑ=18076020025 
* Οι έξι πρώτοι αριθμοί αποτελούν την ημερομηνία γέννησης πχ  180760
* Οι τρείς επόμενοι αποτελούν αριθμούς που δίδει η μηχανογράφηση 
* Ο δέκατος είναι η ένδειξη του φύλου (1=ανδρας , 2=γυναίκα) οι ζυγοί αριθμοί 0,2,4,6,8 δίδονται στις γυναίκες ενώ οι μονοί αριθμοί 1,3,5,7,9 στους άνδρες. 
* Ο τελευταίος (5) είναι [αντικώδικας](https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%B3%CF%8C%CF%81%CE%B9%CE%B8%CE%BC%CE%BF%CF%82_%CF%84%CE%BF%CF%85_%CE%9B%CE%BF%CF%85%CE%BD) 

Φτιάξτε έναν αλγόριθμο ο οποίος θα παίρνει ένα AMKA. Αν ο ΑΜΚΑ δεν είναι στο σωστό φορμάτ, θα πετάει exception. 
Θα πρέπει να ελέγχει ότι: (1) η ημερομηνία υπάρχει και ότι (2) το τελευταίο ψηφίο είναι το σωστό. 

Αν το ΑΜΚΑ είναι στο σωστό φορμάτ τότε θα επιστρέφει True αν ανήκει σε γυναίκα και False αν ανήκει σε άντρα.

Tα διάφορα "κομμάτια" του ΑΜΚΑ θα πρέπει να τα παίρνει με regular expressions.

Δίνεται ο παρακάτω κώδικας ο οποίoς ελέγχει αν μία ημερομηνία είναι σωστή ή όχι (επιτρέφει True αν είναι σωστή και False διαφορετικά)

```python
import datetime

def check_date(year, month, day):
	try:
		datetime.datetime(year=year,month=month,day=day)
	except ValueError:
		return False

	return True

check_date(2019, 2, 28) # Επιστρέφει True
check_date(2019, 2, 29) # Επιστρέφει False
```

Δίνεται ο παρακάτω αλγόριθμος ([κλεμμένος από wikipedia](https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%B3%CF%8C%CF%81%CE%B9%CE%B8%CE%BC%CE%BF%CF%82_%CF%84%CE%BF%CF%85_%CE%9B%CE%BF%CF%85%CE%BD)) ο οποίος ελέγχει αν το τελευταίο ψηφίο του AMKA είναι το σωστό:

```python
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

print (18076020025) # Επιστρέφει True
print (18076020026) # Επιστρέφει False
```

### Άσκηση 4
Οι ελληνικές πινακίδες στα Ι.Χ οχήματα έχουν 2 ή 3 γράμματα ακολουθούμενα από 4 αριθμούς. Τα γράμματα που επιτρέπονται είναι τα Α,Β,Ε,Ζ,Η,Ι,Κ,Μ,Ν,Ο,Ρ,Τ,Υ,Χ (αυτά δηλαδή που υπάρχουν λατινικά αντίστοιχα). Επίσης ο 4ψήφιος αριθμός δεν μπορεί να αρχίζει από 0. Γράψτε **ένα** regular expression το οποίο να αναγνωρίζει αν ένα string περιέχει μία ελληνική πινακίδα. Χρησιμοποιήστε μόνο λατινικούς χαρακτήρες.

π.χ.
```
HPK1234 # OK
HRK0123 # NOT OK 
HCT1234 # NOT OK
HR12345 # NOT OK
HT1234 # OK 
ΗΡΚ12345 # ΝΟΤ ΟΚ
```

### Άσκηση 5
[HLA](https://en.wikipedia.org/wiki/History_and_naming_of_human_leukocyte_antigens)

### Άσκηση 6
Γράψτε ένα regular expression το οποίο θα αναγνωρίζει filenames από αρχεία εικόνας. ραχεία εικόνας θεωρούμε αυτά που τελειώνουν σε .jpg .png και .png. Επίσης θα πρέπει να εξάγει το όνομα του αρχείου (με τη group(1)) και τη κατάληξη του αρχείου (με group(2)).

Π.χ:
```
.bash_profile # Δεν κάνει match
workspace.doc # Δεν κάνει match
img0912.jpg # group(1)--> 'img0912', group(2) --> 'jpg'
updated_img0912.png # group(1)--> 'updated_img0912', group(2) --> 'png'
documentation.html # Δεν κάνει match
favicon.gif # group(1)--> 'favicon', group(2) --> 'gif'
img0912.jpg.tmp # Δεν κάνει match
```


