
### Άσκηση 1

Συμπληρώστε το regular expression στη θέση `...` ώστε η συνάρτηση να εξάγει τον πρώτο ακέραιο αριθμό (μία ή περισσότερες συνεχόμενες ψηφία) από ένα string βιοπληροφορικού ενδιαφέροντος. Μην αλλάξετε την υπόλοιπη συνάρτηση. Αν δεν υπάρχει match, επιστρέφει `None`.

```python
import re

def f(s):
    found = re.search(r'...', s)
    if found:
        return found.group(1)
```

Η συνάρτηση θα πρέπει:
```python
print(f("coverage is 42x on BRCA1")) # Τυπώνει "42"
print(f("GC content 48 percent")) # Τυπώνει "48"
print(f("no digits in this header")) # Τυπώνει None
```

### Άσκηση 2

Συμπληρώστε το regular expression στη θέση `...` ώστε η συνάρτηση να εξάγει ένα pattern: αριθμός ακολουθούμενος από ακριβώς ένα μη ψηφίο (χαρακτήρα που δεν ανήκει στο `0-9`). Μην αλλάξετε την υπόλοιπη συνάρτηση.

```python
import re

def f(s):
    found = re.search(r'...', s)
    if found:
        return found.group(1)
```

Η συνάρτηση θα πρέπει:
```python
print(f("read length 150bp paired-end")) # Τυπώνει "150b"
print(f("mean depth 30x across exon")) # Τυπώνει "30x"
print(f("coverage ends at 42")) # Τυπώνει None
```

### Άσκηση 3

Συμπληρώστε το regular expression στη θέση `...` ώστε η συνάρτηση να εξάγει ένα pattern: αριθμός, μετά ένα μη ψηφίο, μετά άλλο αριθμό (π.χ. κυτταρογενετική ζώνη όπως `17q21`). Μην αλλάξετε την υπόλοιπη συνάρτηση.

```python
import re

def f(s):
    found = re.search(r'...', s)
    if found:
        return found.group(1)
```

Η συνάρτηση θα πρέπει:
```python
print(f("locus 17q21 near BRCA1")) # Τυπώνει "17q21"
print(f("deleted band 1p36 in sample")) # Τυπώνει "1p36"
print(f("chromosome chr17 only")) # Τυπώνει None
```

### Άσκηση 4

Συμπληρώστε το regular expression στη θέση `...` χρησιμοποιώντας υποχρεωτικά τον τελεστή `+`, ώστε η συνάρτηση να εξάγει την πρώτη συνεχόμενη ακολουθία βάσεων DNA από τους χαρακτήρες `A`, `C`, `G`, `T` (κεφαλαία). Μην αλλάξετε την υπόλοιπη συνάρτηση.

```python
import re

def f(s):
    found = re.search(r'...', s)
    if found:
        return found.group(1)
```

Η συνάρτηση θα πρέπει:
```python
print(f("primer=ATGCGATCG end")) # Τυπώνει "ATGCGATCG"
print(f("oligo=GGGCCC ok")) # Τυπώνει "GGGCCC"
print(f("primer=atgcat lower")) # Τυπώνει None
```

### Άσκηση 5

Συμπληρώστε το regular expression στη θέση `...` χρησιμοποιώντας υποχρεωτικά τον τελεστή `*`, ώστε η συνάρτηση να εξάγει τον αριθμό ενός rsID τύπου `rs` ακολουθούμενο από προαιρετικά κενά και μετά ψηφία. Επιστρέφει μόνο τα ψηφία. Μην αλλάξετε την υπόλοιπη συνάρτηση.

```python
import re

def f(s):
    found = re.search(r'...', s)
    if found:
        return found.group(1)
```

Η συνάρτηση θα πρέπει:
```python
print(f("variant rs 12345 pathogenic")) # Τυπώνει "12345"
print(f("variant rs999 reported")) # Τυπώνει "999"
print(f("no snp mentioned here")) # Τυπώνει None
```

### Άσκηση 6

Συμπληρώστε το regular expression στη θέση `...` χρησιμοποιώντας υποχρεωτικά τον τελεστή `?`, ώστε η συνάρτηση να εξάγει μία ακέραια θέση στο γονιδίωμα με προαιρετικό πρόσημο `+` ή `-` στην αρχή (π.χ. `+12345`, `-88`, `12345`). Μην αλλάξετε την υπόλοιπη συνάρτηση.

```python
import re

def f(s):
    found = re.search(r'...', s)
    if found:
        return found.group(1)
```

Η συνάρτηση θα πρέπει:
```python
print(f("position +12345 on forward strand")) # Τυπώνει "+12345"
print(f("position -88 on reverse strand")) # Τυπώνει "-88"
print(f("position 43044295 unstranded")) # Τυπώνει "43044295"
print(f("no numeric position")) # Τυπώνει None
```

### Άσκηση 7

Συμπληρώστε το regular expression στη θέση `...` χρησιμοποιώντας υποχρεωτικά επανάληψη της μορφής `{a,b}`, ώστε η συνάρτηση να εξάγει ένα barcode από βάσεις `A`, `C`, `G`, `T` μήκους από 3 έως 5, αμέσως μετά το κείμενο `barcode=`. Μην αλλάξετε την υπόλοιπη συνάρτηση.

```python
import re

def f(s):
    found = re.search(r'...', s)
    if found:
        return found.group(1)
```

Η συνάρτηση θα πρέπει:
```python
print(f("barcode=ATGC sampleA")) # Τυπώνει "ATGC"
print(f("barcode=GGG sampleB")) # Τυπώνει "GGG"
print(f("barcode=AT sampleC")) # Τυπώνει None
```

### Άσκηση 8

Συμπληρώστε το regular expression στη θέση `...` χρησιμοποιώντας υποχρεωτικά το `^`, ώστε η συνάρτηση να εξάγει το όνομα χρωμοσώματος μόνο όταν βρίσκεται στην αρχή του string (μορφή `chr` ακολουθούμενο από ψηφία ή `X`/`Y`, π.χ. `chr17`, `chrX`). Μην αλλάξετε την υπόλοιπη συνάρτηση.

```python
import re

def f(s):
    found = re.search(r'...', s)
    if found:
        return found.group(1)
```

Η συνάρτηση θα πρέπει:
```python
print(f("chr17\t43044295\t43044296")) # Τυπώνει "chr17"
print(f("chrX\t100\t200")) # Τυπώνει "chrX"
print(f("prefix chr17\t1\t2")) # Τυπώνει None
```

### Άσκηση 9

Συμπληρώστε το regular expression στη θέση `...` χρησιμοποιώντας υποχρεωτικά το `$`, ώστε η συνάρτηση να εξάγει μία ακολουθία βάσεων `A`, `C`, `G`, `T` μόνο όταν βρίσκεται στο τέλος του string. Μην αλλάξετε την υπόλοιπη συνάρτηση.

```python
import re

def f(s):
    found = re.search(r'...', s)
    if found:
        return found.group(1)
```

Η συνάρτηση θα πρέπει:
```python
print(f("read=ATGCCGT")) # Τυπώνει "ATGCCGT"
print(f("seq=GGAA")) # Τυπώνει "GGAA"
print(f("read=ATGCCGT ")) # Τυπώνει None
```

### Άσκηση 10

Συμπληρώστε το regular expression στη θέση `...` χρησιμοποιώντας υποχρεωτικά non-greedy match (`*?`). Η συνάρτηση εξάγει το κείμενο ανάμεσα στο πρώτο `START` και το πρώτο επόμενο `END` (χωρίς τα ίδια τα `START` / `END`). Ανάμεσα υπάρχουν κενά αμέσως μετά το `START` και αμέσως πριν το `END`.


```python
import re

def f(s):
    found = re.search(r'...', s)
    if found:
        return found.group(1)
```

Η συνάρτηση θα πρέπει:
```python
print(f("qual=START dp=10 gene=BRCA1 END noise START dp=2 gene=TTN END")) # Τυπώνει "dp=10 gene=BRCA1"
print(f("x=START only_one END")) # Τυπώνει "only_one"
print(f("no markers here")) # Τυπώνει None
```

### Άσκηση 11

Γράψτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο ένα string και θα επιστρέφει ένα dictionary με named groups μέσω `groupdict()`. Το string περιέχει ένα rsID της μορφής `rs` ακολουθούμενο από ψηφία. Το dictionary έχει το κλειδί `id` με τα ψηφία (χωρίς το `rs`). Αν δεν υπάρχει match, επιστρέφει `None`.

Υπόδειξη για τη μορφή του regular expression: χρησιμοποιήστε named group `(?P<id>...)`.

Η συνάρτηση θα πρέπει:
```python
print(f("reported rs748829059 in clinvar")) # Τυπώνει {'id': '748829059'}
print(f("reported rs9 only")) # Τυπώνει {'id': '9'}
print(f("no snp here")) # Τυπώνει None
```

### Άσκηση 12

Γράψτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο ένα string και θα επιστρέφει dictionary με `groupdict()`. Κάνει match αλλαγή βάσης της μορφής `rs<id>:<ref>><alt>`, όπου `ref` και `alt` είναι μία βάση από `A`, `C`, `G`, `T`. Τα κλειδιά είναι `id`, `ref`, `alt`. Αν δεν υπάρχει match, επιστρέφει `None`.

Η συνάρτηση θα πρέπει:
```python
print(f("change rs123:A>G somatic")) # Τυπώνει {'id': '123', 'ref': 'A', 'alt': 'G'}
print(f("change rs99:T>C")) # Τυπώνει {'id': '99', 'ref': 'T', 'alt': 'C'}
print(f("change rs123:A-G wrong sep")) # Τυπώνει None
```

### Άσκηση 13

Γράψτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο ένα string και θα επιστρέφει dictionary με `groupdict()` για HGVS πρωτεΐνης της μορφής `GENE p.RefPosAlt` (π.χ. `BRAF p.Val600Glu`). Τα κλειδιά είναι `gene`, `ref`, `pos`, `alt`. Το `ref` και το `alt` είναι κωδικοί αμινοξέων 3 γραμμάτων (πρώτο κεφαλαίο, μετά δύο πεζά). Το `pos` είναι ακέραιος. Αν δεν υπάρχει match, επιστρέφει `None`.

Η συνάρτηση θα πρέπει:
```python
print(f("mutation BRAF p.Val600Glu oncogenic")) # Τυπώνει {'gene': 'BRAF', 'ref': 'Val', 'pos': '600', 'alt': 'Glu'}
print(f("mutation TP53 p.Arg273His")) # Τυπώνει {'gene': 'TP53', 'ref': 'Arg', 'pos': '273', 'alt': 'His'}
print(f("mutation BRAF c.1799T>A")) # Τυπώνει None
```

### Άσκηση 14

Γράψτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο ένα string (γραμμή FASTA header UniProt Swiss-Prot) και θα επιστρέφει dictionary με `groupdict()`. Κάνει match την αρχή `sp|<accession>|<entry>`. Τα κλειδιά είναι `accession` και `entry`. Αν η γραμμή δεν είναι Swiss-Prot (`sp|...`), επιστρέφει `None`.

Η συνάρτηση θα πρέπει:
```python
print(f(">sp|P04637|P53_HUMAN Cellular tumor antigen p53")) # Τυπώνει {'accession': 'P04637', 'entry': 'P53_HUMAN'}
print(f(">sp|P38398|BRCA1_HUMAN Breast cancer type 1")) # Τυπώνει {'accession': 'P38398', 'entry': 'BRCA1_HUMAN'}
print(f(">tr|Q8N2C7|EXAMPLE_HUMAN trembl")) # Τυπώνει None
```

### Άσκηση 15

Γράψτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο ένα string και θα επιστρέφει dictionary με `groupdict()` για εγγραφή ClinVar-like της μορφής `Significance|clinvar:<id>|<gene>`. Το `Significance` είναι ακριβώς ένα από: `Pathogenic`, `Benign`, `Uncertain`. Επιτρέπονται προαιρετικά κενά γύρω από τα `|`. Τα κλειδιά είναι `significance`, `clinvar_id`, `gene`. Αν δεν υπάρχει match, επιστρέφει `None`.

Η συνάρτηση θα πρέπει:
```python
print(f("Pathogenic|clinvar:5318|BRCA1")) # Τυπώνει {'significance': 'Pathogenic', 'clinvar_id': '5318', 'gene': 'BRCA1'}
print(f("Benign | clinvar:9 | TTN")) # Τυπώνει {'significance': 'Benign', 'clinvar_id': '9', 'gene': 'TTN'}
print(f("Likely pathogenic|clinvar:1|BRCA2")) # Τυπώνει None
```

### Άσκηση 16

Γράψτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο ένα string (FASTA header) και θα επιστρέφει dictionary με `groupdict()`. Η γραμμή πρέπει να ξεκινάει με `>`, μετά accession με έκδοση (`λέξη.ψηφία`), μετά ακριβώς `Homo sapiens`, μετά σύμβολο γονιδίου. Τα κλειδιά είναι `id`, `organism`, `gene`. Αν δεν υπάρχει match, επιστρέφει `None`.

Η συνάρτηση θα πρέπει:
```python
print(f(">NP_009225.1 Homo sapiens BRCA1 transcript variant 1")) # Τυπώνει {'id': 'NP_009225.1', 'organism': 'Homo sapiens', 'gene': 'BRCA1'}
print(f(">NP_000537.3 Homo sapiens TP53 isoform a")) # Τυπώνει {'id': 'NP_000537.3', 'organism': 'Homo sapiens', 'gene': 'TP53'}
print(f(">NP_009225.1 Mus musculus Brca1")) # Τυπώνει None
```

### Άσκηση 17

Γράψτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο ένα string και θα επιστρέφει λίστα με όλα τα rsID που περιέχει (μορφή `rs` + ψηφία), με τη σειρά εμφάνισης. Χρησιμοποιήστε `re.findall`. Αν δεν υπάρχει κανένα, επιστρέφει κενή λίστα.

Η συνάρτηση θα πρέπει:
```python
print(f("rs1 and rs999 near rs42 in the panel")) # Τυπώνει ['rs1', 'rs999', 'rs42']
print(f("no variants listed")) # Τυπώνει []
```

### Άσκηση 18

Γράψτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο ένα string και θα επιστρέφει `True` αν ολόκληρο το string είναι έγκυρη DNA ακολουθία από κεφαλαία `A`, `C`, `G`, `T` (τουλάχιστον ένας χαρακτήρας), διαφορετικά `False`. Χρησιμοποιήστε `re.match` (ή ισοδύναμο `re.search` με `^` και `$`).

Η συνάρτηση θα πρέπει:
```python
print(f("ATGCGC")) # Τυπώνει True
print(f("ATGxGC")) # Τυπώνει False
print(f("")) # Τυπώνει False
```

### Άσκηση 19

Γράψτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο μία γραμμή BED-like (πεδία χωρισμένα με tab) και θα επιστρέφει dictionary με `groupdict()`. Η μορφή είναι `chrom start end name` στην αρχή της γραμμής. Το `chrom` είναι `chr` ακολουθούμενο από αριθμό ή `X` ή `Y` ή `M`. Τα `start` και `end` είναι ακέραιοι. Το `name` είναι μη κενό χωρίς κενά. Κλειδιά: `chrom`, `start`, `end`, `name`. Αν δεν υπάρχει match, επιστρέφει `None`.

Η συνάρτηση θα πρέπει:
```python
print(f("chr17\t43044295\t43044296\tBRCA1_exon")) # Τυπώνει {'chrom': 'chr17', 'start': '43044295', 'end': '43044296', 'name': 'BRCA1_exon'}
print(f("chrM\t1\t2\tMT_gene")) # Τυπώνει {'chrom': 'chrM', 'start': '1', 'end': '2', 'name': 'MT_gene'}
print(f("17\t1\t2\tno_chr_prefix")) # Τυπώνει None
```

### Άσκηση 20

Γράψτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο ένα string και θα επιστρέφει dictionary με `groupdict()` για HGVS γονιδιωματικής παραλλαγής της μορφής `NC_....:g.<pos><ref>><alt>` (π.χ. `NC_000017.11:g.43044295G>A`). Τα κλειδιά είναι `accession`, `pos`, `ref`, `alt`. Το `accession` είναι `NC_` + ψηφία + `.` + ψηφία. Αν δεν υπάρχει match, επιστρέφει `None`.

Η συνάρτηση θα πρέπει:
```python
print(f("var NC_000017.11:g.43044295G>A germline")) # Τυπώνει {'accession': 'NC_000017.11', 'pos': '43044295', 'ref': 'G', 'alt': 'A'}
print(f("var NC_000013.11:g.32316461A>G")) # Τυπώνει {'accession': 'NC_000013.11', 'pos': '32316461', 'ref': 'A', 'alt': 'G'}
print(f("var NM_007294.4:c.68_69insA")) # Τυπώνει None
```


