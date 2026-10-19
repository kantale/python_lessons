
### General Context
This repository contains (among other things) a list of exercices for students studying bioinformatics with the python language. The main purpose of this repository is to list exercises that the students should do. Below is a list of the exercises for various years. Although this list contains URLs, the files are also located locally in this directory, since this is the directory where the github directory has been cloned. The exercises are in Greek:

### Exercises
* 2021-2022
	* **[Οι ασκήσεις βρίσκονται εδώ](https://github.com/kantale/python_lessons/blob/master/exercises_2022.md)**
* 2020-2021
	* [Σειρά ασκήσεων 1](https://github.com/kantale/python_lessons/blob/master/2020_2021/assignment_1.ipynb). 
	- [Σειρά ασκήσεων 2](https://github.com/kantale/python_lessons/blob/master/2020_2021/assignment_2.ipynb).
	- [Σειρά ασκήσεων 3](https://github.com/kantale/python_lessons/blob/master/2020_2021/assignment_3.ipynb). 
	- [Σειρά ασκήσεων 4](https://github.com/kantale/python_lessons/blob/master/2020_2021/assignment_4.ipynb). 
	- [Σειρά ασκήσεων 5](https://github.com/kantale/python_lessons/blob/master/2020_2021/assignment_5.ipynb). 
- 2019-2020
	- **[ΣΕΙΡΑ ΑΣΚΗΣΕΩΝ 1](https://github.com/kantale/python_lessons/blob/master/2019_2020/assignment_1.md)** 
	- **[ΣΕΙΡΑ ΑΣΚΗΣΕΩΝ 2](https://github.com/kantale/python_lessons/blob/master/2019_2020/assignment_2.md)** 
	- **[ΣΕΙΡΑ ΑΣΚΗΣΕΩΝ 3](https://github.com/kantale/python_lessons/blob/master/2019_2020/assignment_3.md)** 
	- **[ΣΕΙΡΑ ΑΣΚΗΣΕΩΝ 4](https://github.com/kantale/python_lessons/blob/master/2019_2020/assignment_4.md)** 
	- **[ΣΕΙΡΑ ΑΣΚΗΣΕΩΝ 5](https://github.com/kantale/python_lessons/blob/master/2019_2020/assignment_5.ipynb)** 
	- **[Λύσεις στις (περισσότερες) ασκήσεις](https://github.com/kantale/python_lessons/blob/master/2019_2020/solutions_2019.ipynb)**


### STEP 1
Your first task is to just read the files and to understand what this project is about having AI (you) generate new exercises for the 2025_2026 semester. I will give more instruction in the future about what type of exercises you will have to create. For now just say if you understand what this is about or not. If you have any questions let me know. 

### STEP 2
As a second step you will create the first 10 exercises with the following characterists:
* All exercises will request to generate some type of function and will request to "return" the result. 
* All text should be in Greek
* Remember that that the style and content should be the same as other exercises in this repository.
* The exercises will be about understanding basic string operations, python primitive datatypes (int, float, string, boolean, None) and boolean logic.
* Exercises will be generated in file `2025_2026.md`.

### STEP 3
As a third step you will create the next 10 exercises (11 to 20) with the following characterists:
* Append file `2025_2026.md`
* Use the same styling as in STEP 2
* The exercises should be about:
	* 11-15 : basic list operations (no list comprehensions)
	* 16-20 : complex if statements (create complex if..then..else cases including nested ifs)


### STEP 4
As a fourth step you will create the next 10 exercises (21 to 30) with the following characterisitcs:
* All of them will have to be about prime numbers
* All of them have to be implemented by using `while`
* The purpose is to make sure that students understand what `break` and `continue` do
* Some of them should use nested `while`

### STEP 5
As a fifth step you will create the next 10 exercises: (31 to 40) with the following characterisitcs:
* All of them will be about list comprehension
* Some will have to use 2 chained compehensions (for i in b for j in c)
* Some will have to use the if scope inside the comprehension
* Exercises from 35 to 40 will also be about list comprehension but they will have to be solved by using max, min or sum

### STEP 6
As a sixth step you will create the next 10 exercises: (41 to 50) with the following characteristics:
* 41 to 45 will be basic dictionary operations. Contructing dictionaries, Accessing data on dictionaries and iterating over dictionaries
* 46 to 50 will be about dictionary comprehensions. 2 exercises from these should be more advanced that require the combination of lists and dictionaries. 


### STEP 7
As a seventh step you will create the next 10 exercises: (51 to 60) with the following characteristics:
* 51 to 55 will be about basic set operations: Create sets, operations on set, set logic (union, intersection, difference, and complement)
* 56 to 60: Set comprehensions. 58 will require the combination of set and list comprehension. 59 will require the combination of set and dictionary comprehension, number 60 will require the combination of set, list and dictionary comprehension. For 58, 59 and 60 add these requirements in the description. 


### STEP 8
As en eight step you will create the next 10 exercises: (61 to 70) with the following characteristics:
* All of them will be about lambda functions 
* Exercise should be like: Assume that you have a list or dictionaries
* Complete the lambda function in order to achieve a given objective
* The general format of the exercises will be:

Ας υποθέσουμε ότι υπάρχει η ακόλουθη λίστα / dictionary:
```python
data = # <- Add a complex list or a dictionary 
```

Αντικαταστήστε τις τρεις τελείς (...) με τη κατάλληλα lambda συνάρτηση ώστε να τυπώνει...


```python

# One or more of:
result = map(lambda ..., data)  
result = filter(lambda ..., data)  
result = min(data, key=lambda ...)
result = max(data, key=lambda ...)
result = sorted(data, key=lambda ...,)  

print(list(data))
```

### STEP 9
As a ninth step you will have to create exercises 86-90. All of them are about regular expressions. Remember this is a bioinformatics course so all exercises will have to parse some bioinformatics related text. For example variant ID, HGVS, protein name, DNA sequence, compound name, drug ID, gene name, transcript name, etc.

* Exercise 86 Should requite to use some special characters in and the bracket `[]` syntax
* Exercise 87 should require to use \d with the + operator 
* Exercise 88 should requre the combination \d \w the + and the * operator
* Exercise 89 shold require to use the start ^ or the end $ operator 
* Exercise 90 should require to use non greedy operator (?)


### STEP 10
Write exercises from 91 to 95. These exercises will be about python classes and object oriented programming. Each new exercise will require the previous to work. It will be about creating one or more classes representing entities from the bioinformatics domain and gradually add functionality. Each exercise should contain 1-2 lines of code containig the expected class behaviour. Something like:
```python
my_gene = Gene(name='BRCA1')
print(my_gene) # It shoud print 'BRCA1'
```

These exercises should include:
* Create a class, add an initialization 
* Add member functions. Use the member functions from inside and outside the classes 
* Operator overloading (i.e. add)
* `__str__`
* Create another class that "uses" objects from the previous class. (For example a collection of entities)
* Use of `__len__` and `__iter__`

Description should be in the same spirit as other exercises in this file.

# STEP 11
Check exercises from 71 to 79. Create a new exercise (exerise number 96) that will require to re-implement these exerices (71-79) by using object oriented programming. Make sure to include:
   * create a class named `ExclusionPanel` that is initialized through a filename.
   * Create a class named `ExcludedSample`, preferrable a DataClass that will hold each line in the file. Be very descriptive on what that means and provide examples.
   * Make sure that class `ExclusionPanel` manages `ExcludedSample`  
   * Add methods to `ExclusionPanel` to implement all exercises.


# STEP 12 
Exercises 97 to 101 should be about creating plots through matplotlib. All these exercises will be bases on the file [gencode.v49.annotation.gtf.gz](https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_49/gencode.v49.annotation.gtf.gz) this file contains the human genome annotation from [GENCODE](https://www.gencodegenes.org/human/) and is in [GTF format](https://www.ensembl.org/info/website/upload/gff.html). 

Below are the first 10 lines of the file:

```bash
gunzip -c gencode.v49.annotation.gtf.gz| head
```

```
##description: evidence-based annotation of the human genome (GRCh38), version 49 (Ensembl 115)
##provider: GENCODE
##contact: gencode-help@ebi.ac.uk
##format: gtf
##date: 2025-07-08
chr1	HAVANA	gene	11121	24894	.	+	.	gene_id "ENSG00000290825.2"; gene_type "lncRNA"; gene_name "DDX11L16"; level 2; tag "overlaps_pseudogene";
chr1	HAVANA	transcript	11121	14413	.	+	.	gene_id "ENSG00000290825.2"; transcript_id "ENST00000832824.1"; gene_type "lncRNA"; gene_name "DDX11L16"; transcript_type "lncRNA"; transcript_name "DDX11L16-260"; level 2; tag "TAGENE";
chr1	HAVANA	exon	11121	11211	.	+	.	gene_id "ENSG00000290825.2"; transcript_id "ENST00000832824.1"; gene_type "lncRNA"; gene_name "DDX11L16"; transcript_type "lncRNA"; transcript_name "DDX11L16-260"; exon_number 1; exon_id "ENSE00004248723.1"; level 2; tag "TAGENE";
chr1	HAVANA	exon	12010	12227	.	+	.	gene_id "ENSG00000290825.2"; transcript_id "ENST00000832824.1"; gene_type "lncRNA"; gene_name "DDX11L16"; transcript_type "lncRNA"; transcript_name "DDX11L16-260"; exon_number 2; exon_id "ENSE00004248735.1"; level 2; tag "TAGENE";
chr1	HAVANA	exon	12613	12721	.	+	.	gene_id "ENSG00000290825.2"; transcript_id "ENST00000832824.1"; gene_type "lncRNA"; gene_name "DDX11L16"; transcript_type "lncRNA"; transcript_name "DDX11L16-260"; exon_number 3; exon_id "ENSE00003582793.1"; level 2; tag "TAGENE";
```

Based on the contents of this file create exercises that will require to plot part of the information that exists on the file. Try to add some biological meaning to the exercises. 

* Exercise 97 will require to perform a simple ax.plot of a single scalar value. 
* Exercise 98 will require to perform 3 different plots in the same graph. The X axes should be the same for all plots but Y will change. Something like ax.plot(X, Y1), ax.plot(X,Y2), ax.plot(X,Y3)
* Exercise 99 will require to perfom an ax.twinx() and to plot different values on the left Y axes and on the right axes 
* Exercise 100 will require to perform a plot within a plot with the use of fig.add_axes
* Exercise 101 will require to perform a grid of plots (i.e 2 X 3) with the use of plt.subplots(X,Y)

* Make sure to ask from all exercise to use proper titles, labels and legends. 

# STEP 13
Exercise 97 would be better completed with a barplot as it is described now. Alter it so that suits better the ax.plot command 

# STEP 14
Change exercise 98 so that it will reuire the cumulative sum of genes, transcripts and exons, so that ax.plot() is more suitable. 

# STEP 15 
Now it is time to write the description of the final exams of the lessons.  

# STEP 16
In file `exercise.py` write python code that will create a python structure with random data. The structure should be complex i.e. containing a dictionary of list of dictionaries or something similar. 

Suggest three exercises based on this structure that will require to perform some complex transformation or to compute a min,max or sum value. Add a bioinformatics context in this exercise. Each exercises should not take more 10 lines of code to implement.

# STEP 17
Below there are two exercises that have to do with opening files, processing their data, applying some transformation and saving the output in new files. Create 3 similar exercises in file `step_17.md`. The text describing the exercise should be in Greek.  

### Ex. 1
Ο παρακάτω κώδικας δημιουργεί το αρχείο: `thema_5_in.txt` με τα εξής δεδομένα:
```python
data = '''Gene_1=dis_9,dis_6,dis_8,dis_10,dis_5
Gene_2=dis_9,dis_7,dis_8,dis_5,dis_3
Gene_3=dis_5,dis_2,dis_7
Gene_4=dis_5,dis_3,dis_7
Gene_5=dis_5,dis_2,dis_4
Gene_6=dis_9,dis_7,dis_4,dis_1,dis_5
Gene_7=dis_9,dis_8,dis_10,dis_4,dis_5
Gene_8=dis_10,dis_4,dis_3
Gene_9=dis_7,dis_6,dis_8,dis_10,dis_4
Gene_10=dis_3,dis_6,dis_1,dis_7'''

with open('thema_5_in.txt') as f:
	f.write(data)
```

Φτιάξτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο το path και το όνομα ενός αρχείο το οποίο θα έχει την ίδια δομή όπως το `thema_5_in.txt`. Υποθέτουμε ότι το αρχείο αυτό σε κάθε γραμμή έχει το όνομα ενός γονιδίου (`Gene_XYZ`) και τα ονόματα κάποιων ασθενειών (`dis_XYZ`, όπου `XYZ` αριθμός) με τις οποίες το γονίδιο έχει συσχετιστεί. Η συνάρτηση θα πρέπει να φτιάχνει ένα αρχείο με το όνομα `thema_5_out.txt`. Στο αρχείο αυτό κάθε γραμμή θα περιέχει μία ασθένεια (`dis_XYZ`) και τα ονόματα των γονιδίων τα οποία έχουν συσχετιστεί με αυτή. Το αρχείο θα έχει την ίδια μορφοποίηση. Επίσης θα πρέπει οι γραμμές να είναι ταξινομημένες σύμφωνα με τον αριθμό που υπάρχει στο όνομα της ασθένειας. Για παράδειγμα θα πρέπει:

```python
f('thema_5_in.txt', 'thema_5_out.txt')

with open('thema_5_out.txt') as f:
    for l in f:
        print (l.strip())
```
Τυπώνει:
```text
dis_1=Gene_6,Gene_10
dis_2=Gene_3,Gene_5
dis_3=Gene_2,Gene_4,Gene_8,Gene_10
dis_4=Gene_5,Gene_6,Gene_7,Gene_8,Gene_9
dis_5=Gene_1,Gene_2,Gene_3,Gene_4,Gene_5,Gene_6,Gene_7
dis_6=Gene_1,Gene_9,Gene_10
dis_7=Gene_2,Gene_3,Gene_4,Gene_6,Gene_9,Gene_10
dis_8=Gene_1,Gene_2,Gene_7,Gene_9
dis_9=Gene_1,Gene_2,Gene_6,Gene_7
dis_10=Gene_1,Gene_7,Gene_8,Gene_9
```

### Ex. 2
Η παρακάτω συνάρτηση με το όνομα create_5 δημιουργεί ένα αρχείο με το όνομα ask_5.txt. Τα περιεχόμενα του αρχείου είναι:
```
Name=Alex,Values=5,4,3,2
Name=Helen,Values=3,4,7,8
Name=Kostas,Values=9,5,4,3
Name=Maria,values=10,11,12,13
```

```python

def create_5():
    with open('ask_5.txt', 'w') as f:
        f.write('Name=Alex,values=5,4,3,2\n')
        f.write('Name=Helen,values=3,4,7,8\n')
        f.write('Name=Kostas,values=9,5,4,3\n')
        f.write('Name=Maria,values=10,11,12,13\n')
        
    print ('I just created the file: ask_5.txt')
```

Φτιάξτε μία συνάρτηση η οποία θα παίρνει μία παράμετρο η οποία θα είναι string. Η παράμετρος θα περιέχει τη διαδρομή και το όνομα ενός αρχείου με την ίδια δομή όπως το `ask_5.txt`. Η συνάρτηση πρέπει να επιστρέφει μία λίστα. Για κάθε γραμμή του αρχείου η λίστα θα περιέχει ένα dictionary με τα εξής κλειδιά:

* `Name`: Περιέχει ένα string με αυτό που ακολουθεί το `=` μετά το `Name`.
* `values`: Περιέχει μία λίστα με ακέραιους οι οποίοι είναι οι τιμές που ακολουθούν το `=` μετά το `values`.

Για παράδειγμα θα πρέπει:

```python
create_5()
f('ask_5.txt') 
```

Επιστρέφει τη λίστα:

```python
[
    {'name': 'Alex', 'values': [5,4,3,2]},
    {'name': 'Helen', 'values': [3,4,7,8]},
    {'name': 'Kostas', 'values': [9,5,4,3]},
    {'name': 'Maria', 'values': [10,11,12,13]},
]
```


