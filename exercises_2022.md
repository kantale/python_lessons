# Λίστα με ασκήσεις

## Σημειώσεις για όλες τις ασκήσεις
* **ΑΠΑΓΟΡΕΥΕΤΑΙ** να κάνετε: ```a = input("...")``` (και γενικότερα μην το κάνετε ποτέ αυτό..)
* Όταν η εκφώνηση λέει ότι πρέπει να φτιάξετε συνάρτηση.. πρέπει να φτιάξετε συνάρτηση!
* Αν η εκφώνηση λέει ότι η συνάρτηση πρέπει να επιστρέφει κάτι.. τότε μέσα στη συνάρτησή σας πρέπει κάπου να κάνετε ```return```.
* **AΠΑΓΟΡΕΥΕΤΑΙ** να κάνετε: ```return True```  ή ```return False```  (αν το χρησιμοποιείσετε χάνετε τη μισή άσκηση)


Για παράδειγμα, έστω ότι η άσκηση λέει: 

Φτιάξτε μία συνάρτηση σε python η οποία θα παίρνει σαν όρισμα έναν αριθμό. Η συνάρτηση θα πρέπει να επιστρέφει:
* ```True``` αν ο αριθμός είναι μονός
* ```False``` αν ο αριθμός είναι ζυγός (άρτιος).

Τι να **ΜΗΝ** κάνετε:
```python
def f(n):
    if n%2 == 1:
        return True
    else:
        return False

```

Τι να κάνετε:
```python
def f(n):
    return n%2 == 1
```

* **ΑΠΑΓΟΡΕΥΕΤΑΙ** Να χρησιμοποιήσετε τα εξής ονόματα μεταβλητών: `str`, `id`, `int`, `list`, `tuple`, `dict`. Αυτά είναι ονόματα συναρτήσεων της python. Η python σας αφήνει να τα χρησιμοποιήσετε με το "κόστος" ότι χάνεται η αρχική τους χρήση. π.χ:

```python
print (str(55))

str = 'Mitsos'
print (str(55))
```  

### Άσκηση 1
Φτιάξτε μία συνάρτηση η οποία θα παίρνει 2 ορίσματα τα οποία θα είναι αριθμοί (δεν χρειάζεται να το ελέγξετε αυτό). Η συνάρτηση θα επιστρέφει τον μέσο όρο των δύο αριθμών. Για παράδειγμα θα πρέπει:

```python
print (f(3,5)) # Τυπώνει 4
```

### Άσκηση 2
Φτιάξτε μία συνάρτηση η οποία θα παίρνει 2 ορίσματα, έστω Α και Β. Και τα 2 θα είναι tuples με 2 αριθμούς το κάθε ένα (δεν χρειάζεται να το ελέγξετε αυτό). Η συνάρτηση θα επιστρέφει ένα tuple το οποίο θα περιέχει τις συντεταγμένες του μέσου της ευθύγραμμου τμήματος που ορίζεται από τα σημεία Α και Β στον δι-διάστατο χώρο. Για παράδειγμα θα πρέπει:

```python
A = (3,8)
B = (2,5)

print (f(A, B)) # Τυπώνει: (2.5, 6.5)
``` 

**ΠΡΟΣΟΧΗ! Είναι υποχρεωτικό να χρησιμοποιήσετε τη συνάρτηση της άσκησης 1**

Δίνεται ότι αν x<sub>1</sub>, y<sub>1</sub> είναι οι συντεραγμένες του σημείου Α και x<sub>2</sub>, y<sub>2</sub> είναι οι συντεταγμένες του σημείου Β τότε οι συντενταγμένες του μέσου του ευθύγραμου τμήματος ΑΒ είναι (x<sub>1</sub>+x<sub>2</sub>)/2, (y<sub>1</sub>+y<sub>2</sub>)/2 .

### Άσκηση 3
Φτιάξτε μία συνάρτηση η οποία θα παίρνει 2 ορίσματα, έστω Α και Β. Και τα 2 θα είναι tuples με 2 αριθμούς το κάθε ένα (δεν χρειάζεται να το ελέγξετε αυτό). Έστω ότι οι 2 παράμετροι ορίζουν τα αντίστοιχα 2 σημεία Α,Β στον 2-διάστατο χώρο. 
* Αν τα 2 σημεία Α,Β ταυτίζονται στον 2-διάστατο χώρο, τότε η συνάρτηση θα πρέπει να επιστρέφει το string "δεν υπάρχει ευθεία"
* Αν τα Α και Β ανήκουν σε μία ευθεία παράλληλη στον άξονα Y, τότε η συνάρτηση θα πρέπει να επιστρέφει το string "κάθετη". 
* Διαφορετικά θα πρέπει να επιστρέφει τον συντελεστή διεύθυνσης της ευθείας που ορίζεται από τα Α και Β. Ο [συντελεστής διεύθυνσης](https://en.wikipedia.org/wiki/Slope) μίας ευθείας που περνάει από τo σημεία Α με συντεταγμένες: x<sub>1</sub>, y<sub>1</sub>  και από το σημείο Β με συντεταγμένες x<sub>2</sub>, y<sub>2</sub> είναι: λ=(y<sub>2</sub>-y<sub>1</sub>)/(x<sub>2</sub>-x<sub>1</sub>). Για παράδειγμα θα πρέπει:

```python
A = (3,7)
B = (2,5)
print (f(A,B)) # Τυπώνει: 2.0 , (Δηλαδή: (5-7)/(2-3))

Α = (3,7)
Β = (3,10)
print (f(A,B)) # Τυπώνει "κάθετη"

A=(3,7)
B=(3,7)
print (f(A, B)) # Τυπώνει "δεν υπάρχει ευθεία"
```

### Άσκηση 4
Φτιάξτε μία συνάρτηση η οποία θα παίρνει 2 ορίσματα, έστω Α και Β. Και τα 2 θα είναι tuples με 2 αριθμούς το κάθε ένα (δεν χρειάζεται να το ελέγξετε αυτό). Έστω ότι οι 2 παράμετροι ορίζουν τα αντίστοιχα 2 σημεία Α,Β στον 2-διάστατο χώρο. 
* Αν τα 2 σημεία Α,Β ταυτίζονται στον 2-διάστατο χώρο, τότε η συνάρτηση θα πρέπει να επιστρέφει το string "δεν υπάρχει ευθεία"
* Αν τα Α και Β ανήκουν σε μία ευθεία παράλληλη στον άξονα Χ, τότε η συνάρτηση θα πρέπει να επιστρέφει το string "οριζόντια". 
* Διαφορετικά θα πρέπει να επιστρέφει τον συντελεστή διεύθυνσης της ευθείας που είναι κάθετη στην ευθεία που ορίζεται από τα Α και Β.

Δίνεται ότι αν ο συντελεστής διεύθυνσης μίας ευθεία που δεν είναι παράλληλη στον άξονα Χ είναι λ, τότε ο συντελεστής διεύθυνσης της κάθετής της είναι: λ<sup>'</sup> = -1/λ

Για παράδειγμα θα πρέπει:
```python
A = (3,7)
B = (2,5)
print (f(A,B)) # Τυπώνει: -0.5 , (Δηλαδή: -1/((5-7)/(2-3))  )

Α = (3,7)
Β = (0,7)
print (f(A,B)) # Τυπώνει "οριζόντια"

A=(3,7)
B=(3,7)
print (f(A, B)) # Τυπώνει "δεν υπάρχει ευθεία"

```

**Είναι υποχρεωτικό να χρησιμοποιήσετε τη συνάρτηση της άσκησης 3**

### Άσκηση 5
Φτιάξτε μία συνάρτηση η οποία θα παίρνει 4 ορίσματα: το c, το r, το a και το b. Το c θα είναι είναι tuple το οποία θα περιέχει 2 αριθμούς και τα r,a,b θα είναι αριθμοί (δεν χρειάζεται να τα ελέγξετε αυτά). Ας υποθέσουμε ότι το c αντιπροσωπεύει το κέντρο ενός κύκλου στον 2-διάστατο χώρο, ότι r είναι η ακτίνα του και ότι υπάρχει η ευθεία ε η οποία ορίζεται από την εξίσωση: y=aχ+b. 
* Αν το κέντρο του κύκλου c ΔΕΝ ανήκει στην ευθεία ε τότε η συνάρτηση πρέπει να επιστρέφει το string "το κέντρο δεν ανήκει στην ευθεία"
* Διαφορετικά θα πρέπει να επιστρέφει 2 tuples, το κάθε ένα με 2 αριθμούς. Τα 2 tuples θα πρέπει να περιέχουν τις συντεταγμένες των 2 σημείων όπου η ευθεία ε τέμνει τον κύκλο. 

Για παράδειγμα:
```python
c = (0, 0)
r = 1
a = 1
b = 0

point_1, point_2 = f(c, r, a, b) # Τυπώνει: (, ))
print (point_1) # Τυπώνει (-0.7071067811865476, -0.7071067811865476)
print (point_2) # Τυπώνει (0.7071067811865476, 0.7071067811865476)


c = (1, 1)
r = 1
a = 1
b = 0

print (f(c, r, a, b)) # Τυπώνει: "το κέντρο δεν ανήκει στην ευθεία"

```

Βοήθεια:

1. Έστω K,L οι συντεταγμένες του κέντρου. Αν η ευθεία y=aχ+b περνάει από το κέντρο θα πρέπει να ισχύει: L = a * K + b   
2. Έστω ότι ένα σημείο που ανήκει στην ευθεία ε και ανήκει στον κύκλο έχει συντεταγμένες: x,y. Θα πρέπει να ισχύει:
   1. y=a * x + b  (αφού ανήκει στην ευθεία)
   2. (x-K)^2 + (y-L)^2 = r^2  (αφού ανήκει στον κύκλο)
   3. Αν αντικαταστήσουμε στην εξίσωση (ii) το y από την εξίσωση (i), θα έχουμε: (x-K)^2 + ((a * x + b)-L)^2 = r^2
   4. Αν λύσουμε αυτή την εξίσωση τότε θα δούμε ότι [έχει δύο λύσεις](https://i.imgur.com/rnuKi3W.png). Για κάθε ένα από αυτά τα "χ" μπορούμε να υπολογίσουμε το αντίστοιχο y από την εξίσωση της ευθείας (y = a * x + b)
3. Για τη τετραγωνική ρίζα μπορείτε να χρησιμοποιήσετε έναν από τους παρακάτω τρόπους:

```python
from math import sqrt

print (sqrt(16))
print (16**0.5)
```

### Άσκηση 6 
Φτιάξτε μία συνάρτηση η οποία θα παίρνει 4 ορίσματα: a,b,P,d. Τα a,b,d θα είναι αριθμοί και το P θα είναι ένα tuple το οποίο θα αποτελείται από 2 αριθμούς (δεν χρειάζεται να το ελέγξετε αυτό). 
* Αν το σημείo P που ορίζεται από τις συντεταγμένες που υπάρχουν στο tuple P **ΔΕΝ** ανήκει στην ευθεία ε που ορίζεται από την εξίσωση: y=ax+b. Τότε επιστρέφει το string "λάθος"
* Διαφορετικά θα πρέπει να επιστρέφει 2 tuples, το κάθε ένα με 2 αριθμούς. Τα 2 tuples θα πρέπει να περιέχουν τις συντεταγμένες των 2 σημείων πάνω στην ευθεία ε που απέχουν από το σημείο P απόσταση d.

Δηλαδή θα πρέπει:
```python
a=1
b=0
P=(0,0)
d=1

point_1, point_2 = f(a,b,P,d)
print (point_1) # Τυπώνει (-0.7071067811865476, -0.7071067811865476)
print (point_2) # Τυπώνει (0.7071067811865476, 0.7071067811865476)

a=1
b=0
P=(1,1)
d=1
print (f(a,b,P,d)) # Τυπώνει "λάθος"
```

**Είναι υποχρεωτικό να χρησιμοποιήσετε την συνάρτηση της άσκησης 5**

### Άσκηση 7
Φτιάξτε μία συνάρτηση η οποία θα παίρει 2 ορίσματα Α,Β. Τα Α και Β θα είναι tuples με 2 αριθμούς το κάθε ένα (δεν χρειάζεται να το ελέγξετε αυτό).
* Αν τα Α και Β ταυτίζονται θα πρέπει να επιστρέφει τo string "λάθος"
* Διαφορετικά θα επιστρέφει ένα tuple με δύο αριθμούς. Το tuple αυτό θα είναι οι συντεταγμένες του μοναδικού σημείου P το οποίο έχει τις εξής ιδιότητες:
   * Ανήκει στην ευθεία που ορίζεται από τα 2 σημεία Α και Β
   * Απέχει από το Α τόσο όσο η απόσταση μεταξύ των Α και Β
   * Δεν είναι το Β

Για παράδειγμα θα πρέπει:
```python
A = (0,0)
B = (1,0)

print (f(A,B)) # Επιστρέφει: (-1, 0)
```

**Είναι υποχρεωτικό να χρησημποιήσετε τη συνάρτηση της άσκησης 5**



### Άσκηση 8
Φτιάξτε μία συνάρτηση η οποία θα παίρνει 3 ορίσματα Α,Β,d. Τα Α και Β θα είναι tuples με 2 αριθμούς το κάθε ένα και το d θα είναι ένας αριθμός (δεν χρειάζεται να το ελέγξετε αυτό). 
* Αν τα 2 σημεία στον 2-διάστατο χώρο που ορίζονται από τις συντεταγμένες που υπάρχουν στα tuples Α και Β ταυτίζονται, τότε θα πρέπει να επιστρέφει τo string "λάθος".
* Διαφορετικά επιστρέφει 2 tuples, το κάθε ένα με 2 αριθμούς. Το κάθε tuple εκπροσωπεί τα 2 σημεία Κ,Λ τα οποία ανήκουν στη μεσοκάθετο της Α,Β και απέχουν από το μέσο της Α,Β απόσταση d.

Βοήθεια:
1. Υπολογίστε το μέσο της Α,Β (συνάρτηση άσκησης 2), έστω Γ.
2. Υπολογίστε το slope της κάθετης στην Α,Β, (συνάρτηση άσκησης 4) , έστω λ<sup>'</sup>
3. Αν η εξίσωση της μεσοκαθέτου είναι  y = ax + b. Τότε: a = λ<sup>'</sup>. Γνωρίζουμε ένα σημείο πάνω στην μεσοκάθετο, (το Γ) οπότε μπορούμε να υπολογίσουμε το b.
4. Αφού ξέρουμε τα a,b της ευθείας της μεσοκαθέτου, ένα σημείο πάνω στη μεσοκάθετο (το Γ) και την απόσταση d, μπορούμε να χρησιμοποιήσουμε τη συνάρτηση της άσκησης 5 για να υπολογίσουμε τα Κ,Λ

**Είναι υποχρεωτικό να χρησιμοποιήσετε της συναρτήσεις των ασκήσεων 2,4 και 5**

Για παράδειγμα θα πρέπει:

```python
Α = (-0.7071067811865476, +0.7071067811865476)
Β = (0.7071067811865476, -0.7071067811865476)
d = 1

point_1, point_2 = f(A, B, d)
print (point_1) # Τυπώνει: (-0.7071067811865476, -0.7071067811865476)
print (point_2) # Τυπώνει: (+0.7071067811865476, +0.7071067811865476)
```

### Άσκηση 9
Φτιάξτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο 3 αριθμούς: a,b,tolerance. Η παράμετρος tolerance θα έχει τη default τιμή: 0.00001 . 
* Αν η απόλυτη διαφορά των a και b είναι μικρότερη από το tolerance τότε επιστρέφει `True`
* Διαφορετικά επιστρέφει `False`

**Προσοχή! H συνάρτηση ΔΕΝ επιστρέφει κάποιο string!**

Για παράδειγμα θα πρέπει:
```python
print (f( 1.2345678,  1.234587)) # Επιστρέφει False
print (f( 1.2345678,  1.234587, tolerance = 0.0001)) # Επιστρέφει True
```

### Άσκηση 10
Φτιάξτε μία συνάρτηση η οπoία θα παίρνει σαν παράμετρο ένα string το οποίο αναπαριστάει μία ημερομηνία με το εξής φορμάτ: MM/DD/YYYY (αμερικάνικο). Για παράδειγμα η ημερομηνια 1 Δεκεμβρίου 2022 αναπαριστάται ως: 12/01/2022. Η συνάρτηση θα πρέπει να επιστρέφει ένα string με την ίδια ημερομηνία αλλά με το φορμάτ DD/MM/YYYY (Ευρωπαϊκό). Για παράδειγμα θα πρέπει:

```python
print (f('12/01/2022')) # Επιστρέφει '01/12/2022'
```
**Απαγορεύεται να χρησιμοποιήσετε regular expressions!**

### Άσκηση 11 
Φτιάξτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο μία λίστα από αριθμούς (δεν χρειάζεται να το ελέγξετε αυτό). Η συνάρτηση θα επιστρέφει το άθροισμα του διπλάσιου των αριθμών της λίστας που ανήκουν στο κλειστό διάστημα [10, 20]. Για παράδειγμα θα πρέπει:

```python
l = [3,15,7,8,12,20,3]
print (f(l)) # επιστρέφει 94 (15*2 + 12*2 + 20*2)
``` 

* Είναι υποχρεωτικό να χρησιμοποιήσετε `map`, `filter`.
* Μη χρησιμοποιήσετε list comprehension
* Μη χρησιμοποιήσετε `for`, `while`

### Άσκηση 12 
Φτιάξτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο μία λίστα από αριθμούς (δεν χρειάζεται να το ελέγξετε αυτό). Η συνάρτηση θα επιστρέφει το άθροισμα του διπλάσιου των αριθμών της λίστας που ανήκουν στο κλειστό διάστημα [10, 20]. Για παράδειγμα θα πρέπει:

```python
l = [3,15,7,8,12,20,3]
print (f(l)) # επιστρέφει 94 (15*2 + 12*2 + 20*2)
``` 

* Είναι υποχρεωτικό να χρησιμοποιήσετε list comprehension 
* Μη χρησιμοποιήσετε `map`, `filter`
* Μη χρησιμοποιήσετε `for`, `while` (εκτός από το `for` του list comprehensio)


### Άσκηση 13 
Φτιάξτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο 2 λίστες a,b. Η κάθε λίστα θα περιέχει tuples με 2 αριθμούς το κάθε ένα (δεν χρειάζεται να το ελέγξετε αυτό). H συνάρτηση θα πρέπει να επιστρέφει την μεγαλύτερη απόσταση μεταξύ όλων των σημείων του a και όλων των σημείων του b.

Για παράδειγμα:
```python
a = [(9.68, 9.55), (4.99, 8.97), (8.67, 6.28), (5.98, 8.99), (7.54, 0.94), (0.04, 7.76), (5.47, 7.83), (8.78, 0.17), (1.4, 4.45), (6.74, 2.76)]
b = [(8.02, 6.82), (2.08, 4.8), (1.85, 5.42), (9.92, 8.86), (0.84, 7.62)]

print (f(a,b)) # Τυπώνει: 10.887887765769815 
```
* Είναι υποχρεωτικό να χρησιμοποιήσετε list comprehension 
* Ως απόσταση εννοείται η ευκλείδεια απόσταση

### Άσκηση 14
Φτιάξτε μία συνάρτηση, έστω `f1` η οποία θα παίρνει 3 παραμέτρους. O πρώτος (έστω K) θα είναι ένα tuple με 2 αριθμούς, ο δεύτερος και ο τρίτος (έστω r και phi) θα είναι αριθμοί (δεν χρειάζεται να τα ελέγξετε αυτά). Η συνάρτηση θα επιστρέφει ένα tuple το οποίο περιέχει 2 αριθμούς. Οι αριθμοί αυτοί θα είναι οι συντεταγμένες του σημείου P το οποίο έχει τις εξής ιδιότητες:
* Το P ανήκει πάνω στον κύκλο με κέντρο το K και ακτίνα r 
* H ευθεία που ορίζεται από το ευθύγραμμο τμήμα ΡΟ σχηματίζει γωνία phi μοίρες με τον άξονα X'X. 

Για παράδειγμα θα πρέπει:

```python
K = (0,0)
r = 1
phi = 45

print (f(K,r,phi)) # Τυπώνεθ: (0.7071067811865476, 0.7071067811865476)


K = (0,0)
r = 1
phi = 90

f(K,r,phi) # Τυπώνει: (0.0, 1.0)
```


Δίνεται πως μπορείτε να υπολογίσετε το ημίτονο και συνημίτονο των phi μοιρών (αν το χρειαστείτε!):
```python
from math import sin, cos, pi

phi = 45
# Ημίτονο:
sin(phi/360 * 2*pi) # 0.7071067811865475 

# Συνημίτονο:
cos(phi/360 * 2*pi) # 0.7071067811865475 
```

Φτιάξτε μία συνάρτηση με το όνομα ```f2``` η οποία θα παίρνει σαν παράμετρο 3 αριθμούς: O πρώτος (έστω K) θα είναι ένα tuple με 2 αριθμούς, ο δεύτερος (έστω r) θα είναι ένας αριθμός και ο τρίτος (έστω n) θα είναι ένας ακέραιος αριθμός (δεν χρειάζεται να τα ελέγξετε αυτά). Η συνάρτηση θα επιστρέφει μία λίστα με tuples. Κάθε tuple θα έχει δύο αριθμούς. Η λίστα θα περιέχει όλα τα σημεία τα οποία έχουν τις εξής ιδιότητες:
* Όλα τα σημεία ανήκουν στον κύκλο που έχει κέντρο Κ και ακρίνα r
* Τα σημεία σχηματίζουν ένα [κανονικό πολύγωνο τάξης n](https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CE%BD%CE%BF%CE%BD%CE%B9%CE%BA%CF%8C_%CF%80%CE%BF%CE%BB%CF%8D%CE%B3%CF%89%CE%BD%CE%BF).
* Το σημείο (K[0]+r, K[1]) είναι υποχρεωτικό να υπάρχει στη λίστα που επιστρέφετε. 

Σημείωσεις:
* Είναι υποχρεωτικό να χρησιμοποιήσετε τη συνάρτηση `f1`.
* Είναι υποχρεωτικό να χρησιμοποιήσετε list comprehension 
* Απαγορεύεται να χρησιμοποιήσετε numpy (και.. συναφείς βιβλιοθήκες)

Για παράδειγμα θα πρέπει:
```python
K = (0,0)
r = 1

print (f(K, r, n=3)) # Τυπώνει:  [(1.0, 0.0), (-0.4999999999999998, 0.8660254037844388), (-0.5000000000000004, -0.8660254037844384)]

print (f(K, r, n=4)) # Τυπώνει:  [(1.0, 0.0), (6.123233995736766e-17, 1.0), (-1.0, 1.2246467991473532e-16), (-1.8369701987210297e-16, -1.0)]

print (f(K, r, n=5)) # Τυπώνει: [(1.0, 0.0), (0.30901699437494745, 0.9510565162951535), (-0.8090169943749473, 0.5877852522924732), (-0.8090169943749475, -0.587785252292473), (0.30901699437494723, -0.9510565162951536)] 
```

### Άσκηση 15 
Δίνεται ο παρακάτω κώδικας ο οποίος φτιάχνει μία λίστα με όλα τα φύλλα της τράπουλας.

```python
suits = list('♠♥♦♣')
symbols = list('23456789JQKA') + ['10']

l = [x+y for x in suits for y in symbols]
print (l)
```

Φτιάξτε μία συνάρτηση η οποία δεν θα παίρνει κανένα όρισμα. Η συνάρτηση θα επιστρέφει μία λίστα με όλα τα φύλλα του παιχνιδιού [UNO](https://en.wikipedia.org/wiki/Uno_%28card_game%29). Όλα τα φύλλα (108) βρίσκονται σε αυτή την εικόνα:

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/UNO_cards_deck.svg/1920px-UNO_cards_deck.svg.png)

Σύμφωνα με τη wikipedia:
> The deck consists of 108 cards: four each of "Wild" and "Wild Draw Four", and 25 each of four colors (red, yellow, green, blue). Each color consists of one zero, two each of 1 through 9, and two each of "Skip", "Draw Two", and "Reverse". These last three types are known as "action cards". 

Για να κωδικοποήσετε τα φύλλα σας χρησιμοποιήστε τους εξής χαρακτήρες:
* Τους χαρακτήρες: `0`,`1`,`2`,`3`,`4`,`5`,`6`,`7`,`8`,`9` για τους αριθμούς
* Τους χαρακτήρες: `R`, `Y`, `G`, `B` για τα χρώματα.
* Τον χαρακτήρα: `Ø` για το `Skip`.
* Τον χαρακτήρα: `⇋` για το `Reverse`.
* Τον χαρακτήρα: `☍` για το `Draw Two (+2)`.
* Τον χαρακτήρα: `⎈` για το `Wild`.
* Τον χαρακτήρα: `⚃` για το `Wild Draw Four`.

Τα φύλλα που έχουν χρώμα αποτελούνται από 2 χαρακτήρες: πρώτα πάει το χρώμα και μετά το είδος (για παράδειγμα: `G9`, `BØ`). 
Θα πρέπει δηλαδή:
```python
print (f()) # Τυπώνει: ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'RØ', 'R⇋', 'R☍', 'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'YØ', 'Y⇋', 'Y☍', 'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'GØ', 'G⇋', 'G☍', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'BØ', 'B⇋', 'B☍', '⎈', '⚃', '⎈', '⚃', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'RØ', 'R⇋', 'R☍', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'YØ', 'Y⇋', 'Y☍', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'GØ', 'G⇋', 'G☍', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'BØ', 'B⇋', 'B☍', '⎈', '⚃', '⎈', '⚃']
```

Σημειώσεις: 
* Η σειρά που τα τυπώνει δεν έχει σημασία. Εσείς μπορείτε να φτιάξετε μία λίστα με διαφορετική σειρά
* Θα πρέπει να τη λύσετε με list comprehension(s) τα οποία θα παράγουν τη ζητούμενη λίστα. 
* Bonus: Αν τη λύσετε με *ένα* list comprehension θα πάρετε bonus: 12/10. 

### Άσκηση 16 
Ένα μενού εστιατορίου αποτελείται από 3 ορεκτικά:
```python
orektika = ['ντολμαδάκια', 'φάβα', 'μελιτζανοσαλάτα']
```
Επίσης αποτελείται από 2 σαλάτες:
```python
salates = ['χωριάτικη', 'μαρούλι']
```
Και τρία κύρια πιάτα:
```python
kyria = ['σπλινάντερο', 'γαρδούμπες', 'μοσχαροκεφαλή']
```
Ο σεφ του εστιατορίου λέει ότι ένας πελάτης μπορεί να πάρει οποιαδήποτα συνδοιασμό θέλει (ένα ορκετικό, μία σαλάτα και ένα κυρίος πιάτο), αλλά υπάρχουν οι παρακάτω περιορισμοί:
* Αν ο πελάτης πάρει `'ντολμαδάκια'` για ορεκτικό τότε δεν μπορεί να πάρει `'μοσχαροκεφαλή'` για κύριο πιάτο
* Αν ο πελάτης πάρει `'μαρούλι'` για σαλάτα τότε μπορεί να πάρει μόνο `'σπλινάντερο'` για κύριο πιάτο.

Φτιάξτε μία συνάρτηση η οποία θα παίρνει 3 παράμετρους. Και οι τρεις θα είναι λίστες με τις τιμές που υπάρχουν παραπάνω (δεν χρειάζεται να το ελέγξετε αυτό). Η συνάρτηση θα επιστρέφει μία λίστα με tuples. Κάθε tuple θα έχει και έναν συνδυασμό από ορεκτκό, σαλάτα, κύριο πιάτο. Η λίστα θα περιέχει όλους τους δυνατούς συνδυασμούς που μπορεί να παραγγείλει ένας πελάτης, σεβόμενος τους περιορισμούς του σεφ. 

### Άσκηση 17 
Φτιάξτε μία συνάρτηση η οποία θα παίρνει μία παράμετρο η οποία θα είναι string (δεν χρειάζεται να το ελέγξετε αυτό). Η συνάρτηση θα επιστρέφει ένα string το οποίο θα περιέχει μόνο το πρώτο γράμμα κάθε λέξης του string της παραμέτρου. Για παράδειγμα:

```python
print (f('Πανεπιστήμιο Κρήτης')) # Τυπώνει ΠΚ
print (f('ΕΘΝΙΚΟΣ ΟΡΓΑΝΙΣΜΟΣ ΤΟΥΡΙΣΜΟΥ')) # Τυπώνει ΕΟΤ
``` 

* Θεωρούμε ότι όλες οι λέξεις χωρίζονται με ένα space
* Θα πρέπει να την υλοποιήσετε ή με filter/map ή με list comprehension 
* Δίνεται ότι:
   * Μπορείτε να φτιάξετε μία λίστα με όλα τα γράμματα ενός string:
```python
print (list('hello'))
```
   *  αν θέλετε να ενώσετε όλα τα γράμματα μίας λίστας που αποτελείται από string μπορείτε να χρησιμομποιήσετε τη `''.join`:
```python
a = ['h', 'e', 'l', 'l', 'o']
print (''.join(a))
```

### Άσκηση 18 
Μία παλινδρομική ακολουθία ορίζεται αυτή η οποία μπορεί να διαβαστεί το ίδιο από την αρχή προς το τέλος και από το τέλος προς την αρχή (π.χ: `GCCG`, `GCTGC`)
Φτιάξτε μία συνάρτηση η οποία δεν θα παίρνει καμία παράμερτο. Η συνάρτηση θα επιστρέφει μία λίστα με όλες οι δυνατές ακολουθίες DNA που αποτελούνται από 5 νουκλεοτίδια και είναι παλινδρομικές. 

Δίνεται ο παρακάτω κώδικας ο οποίος παράγει όλες τις ακολουθίες DNA με μέγεθος 3:
```python
[a+b+c for a in 'ACGT' for b in 'ACGT' for c in 'ACGT']
```

### Άσκηση 19
Φτιάξτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο έναν ακέραιο αριθμό n (δεν χρειάζεται να το ελέγξετε αυτό). Η συνάρτηση θα επιστρέφει μία λίστα η οποία θα αποτελείται από λίστες. Η πρώτη υπολίστα θα έχει τον αριθμό 1, η δεύτερη θα έχει τους αριθμούς 1,2 η τρίτη τους αριθμούς 1,2,3 κτλ.. η τελευταία θα έχεις τους αριθμούς 1,2,3,...,n. Για παράδειγμα θα πρέπει:

```python
print (f(3)) # Τυπώνει: [[1], [1,2], [1,2,3]]
print (f(4)) # Τυπώνει: [[1], [1,2], [1,2,3], [1,2,3,4]]
```

### Άσκηση 20
Φτιάξτε μία συνάρτηση η οποία θα παιρνει σαν παράμετρο 2 λίστες α,β. Η πρώτη θα είναι μία λίστα με αριθμούς και η δεύτερη θα είναι μία λίστα με tuples όπου κάθε tuple θα αποτελείται από δύο αριθμούς κ,λ τέτοιους ώστε κ>λ (δεν χρειάζεται να τα ελέγξετε όλα αυτά). Η συνάρτηση θα επιστρέφει μία λίστα η οποία θα περιέχει τους αριθμούς της λίστας α οι οποίοι υπάρχουν σε τουλάχιστον ένα από τα κλειστά διαστήματα που ορίζονται από τα tuples της παραμέτρου β. Για παράδειγμα θα πρέπει:

```python
a = [3,10, 17]
b = [(4,7), (0,1), (13,18), (21,25)]

print (f(a,b)) # Τυπώνει: [17] (μόνο το 17 υπάρχει τουλάχιστον σε ένα από τα διαστήματα της b (το [13, 18]))

a = [3,10, 17]
b = [(4,7), (0,1), (13,18), (16,25)]

print (f(a,b)) # Τυπώνει: [17] (μόνο το 17 υπάρχει τουλάχιστον σε ένα από τα διαστήματα της b (τα [13, 18] και [16,25]))

a = [17, 3,10, 17]
b = [(4,7), (0,1), (13,18), (16,25)]

print (f(a,b)) # Τυπώνει: [17, 17] 


```

**Οι ασκήσεις από εδώ και κάτω δεν έχουν καθαρογραφεί!! Μην ξεκινήσετε την υλοποίησή τους μέχρι να φύγει αυτή η σημείωση!**


### Άσκηση 21

Φτιάξτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο μία λίστα l. Η λίστα θα περιέχει tuples. Κάθε tuple θα περιέχει 2 strings (δεν χρειάζεται να τα ελέγξετε αυτά). Η συνάρτη θα επιστρέφει True/False ανάλογα με το αν υπάρχει έστω και ένα tuple όπου και τα δύο string να αρχίζουμ με φωνήεν. 

Δινεται το παρακάτω string το οποίο περιέχει όλα τα φωνήεν (στα Αγγλικά) για το οποίο πρέπει να ελέγχετε:
```python
vowels = 'AaEeIiOoUu'
```

Για παράδειγμα θα πρέπει:

```python
l  =[('Alexandros', 'Kanterakis'), ('Spiros', 'Mpimpilas'), ('Maria', 'Aliferh')]
print (f(l)) # Τυπώνει False (κανένα ζευγάρι δεν έχει και τα 2 πρώτα γράμματα φωνήεντα )

l  =[('Alexandros', 'Kanterakis'), ('Spiros', 'Mpimpilas'), ('Eleftheria', 'Arvanitaki'), ('Maria', 'Aliferh')]
print (f(l)) # Τυπώνει True 

```

Σημείωση: Είναι υποχρεωτικό να χρησιμοποιήσετε for / break

### Άσκηση 22
Φτιάξτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο μία λίστα l. Η λίστα θα περιέχει tuples. Κάθε tuple θα περιέχει 2 strings (δεν χρειάζεται να τα ελέγξετε αυτά). Η συνάρτη θα επιστρέφει το πλήθος από τα στοιχεία της l στα οποία και τα δύο string αρχίζουμ με φωνήεν. 

Δινεται το string to οποίο περιέχει όλα τα φωνήεν (στα Αγγλικά) για το οποίο πρέπει να ελέγχετε:
```python
vowels = 'AaEeIiOoUu'
```

Για παράδειγμα θα πρέπει:

```python
l = [('Alexandros', 'Kanterakis'), ('Spiros', 'Mpimpilas'), ('Maria', 'Aliferh')]
print (f(l)) # Τυπώνει 0 (κανένα ζευγάρι δεν έχει και τα 2 πρώτα γράμματα φωνήεντα )

l = [('Alexandros', 'Kanterakis'), ('Spiros', 'Mpimpilas'), ('Eleftheria', 'Arvanitaki'), ('Maria', 'Aliferh')]
print (f(l)) # Τυπώνει 1 

l = [('Alexandros', 'Kanterakis'), ('Spiros', 'Mpimpilas'), ('Eleftheria', 'Arvanitaki'), ('Maria', 'Aliferh'),  ('Aristotelhs', 'Onassis')]
print (f(l)) # Τυπώνει 2

```

Σημείωση: Είναι υποχρεωτικό να χρησιμοποιήσετε for / continue

### Άσκηση 23
Φτιάξτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο δύο λίστες a,b. Η κάθε λίστα θα περιέχει strings και οι δύο λίστες θα έχουν το ίδιο μέγεθος (δεν χρειάζεται να τα ελέγξετε αυτά). Υποθέτουμε ότι η πρώτη λίστα θα περιέχει τα ονόματα και η δεύτερη τα επίθετα από μία ομάδα ανθρώπων. Η συνάρτηση θα πρέπει να επιστρέφει το πλήθος των ατόμων όπου και το όνομα αλλά και το επίθετο αρχίζουν από φωνήεν. 

Δινεται το string οποίο περιέχει όλα τα φωνήεν (στα Αγγλικά) για τα οποία πρέπει να ελέγχετε:
```python
vowels = 'AaEeIiOoUu'
```

Για παράδειγμα θα πρέπει:

```python
a = ['Alexandros', 'Spiros', 'Maria']
b = ['Kanterakis', 'Mpimpilas', 'Aliferh']
print (f(a,b)) # Τυπώνει 0 (κανένα ζευγάρι δεν έχει και τα 2 πρώτα γράμματα φωνήεντα )


a = ['Alexandros', 'Spiros', 'Eleftheria', 'Maria']
b = ['Kanterakis', 'Mpimpilas', 'Arvanitaki', 'Aliferh']

print (f(a,b)) # Τυπώνει 1 

a = ['Alexandros', 'Spiros', 'Eleftheria', 'Maria', 'Aristotelhs']
b = ['Kanterakis', 'Mpimpilas', 'Arvanitaki', 'Aliferh', 'Onassis']
print (f(a,b)) # Τυπώνει 2

```

hint: `zip`

### Άσκηση 24 
Φτιάξτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο μία λίστα l. Η λίστα θα περιέχει tuples. Κάθε tuple θα περιέχει 2 strings (δεν χρειάζεται να τα ελέγξετε αυτά). Η συνάρτη θα επιστρέφει ένα string. To string αυτό θα είναι το επίθετο του ονόματος το οποίο είναι πρώτο αλφαβητικά από όλα τα ονόματα στα οποία και το όνομα αλλά και το επίθετο είναι φωνήεντα. Αν δεν υπάρχει όνομα όπου και το όνομα και το επίθετο είναι φωνήεν, θα επιστρέφει `None`. 

Δινεται string το οποίο περιέχει όλα τα φωνήεν (στα Αγγλικά) για το οποίο πρέπει να ελέγχετε:
```python
vowels = 'AaEeIiOoUu'
```

Για παράδειγμα θα πρέπει:

```python
l = [('Alexandros', 'Kanterakis'), ('Spiros', 'Mpimpilas'), ('Maria', 'Aliferh')]
print (f(l)) # Τυπώνει `None` (κανένα ζευγάρι δεν έχει και τα 2 πρώτα γράμματα φωνήεντα )

l = [('Alexandros', 'Kanterakis'), ('Spiros', 'Mpimpilas'), ('Aristotelhs', 'Onassis'), ('Maria', 'Aliferh')]
print (f(l)) # Τυπώνει `Onassis`

l = [('Alexandros', 'Kanterakis'), ('Spiros', 'Mpimpilas'), ('Eleftheria', 'Arvanitaki'), ('Maria', 'Aliferh'),  ('Aristotelhs', 'Onassis')]
print (f(l)) # Τυπώνει 'Arvanitaki'

```

Σημείωση: απαγορεύεται να χρησιμοποιήσετε ταξινόμηση (sort, sorted)

### Άσκηση 25
Στις φετινές πανελλήνιες, στα μαθηματικά, "έπεσε" η μελέτη της συνάρτησης f(x)=e<sup>x</sup>-3x. Η αλλιώς:

```python
import math
def f_no_numpy(x):
    return math.exp(x)-3*x

```

Αν τη πλοτάρουμε για Χ από 0 μέχρι 2 θα πάρουμε την εξής γραφική παράσταση:
![img](data:image/png;base64,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)






