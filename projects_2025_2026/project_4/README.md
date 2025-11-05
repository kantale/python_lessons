# Project 4
In this project, you will analyze real metagenomic sequencing data to estimate how complex a microbial community is or else, how many different organisms it likely contains.

You will do this without using any reference databases (purely from the raw DNA sequences) by examining the diversity of short DNA words (called k-mers) and measuring their Shannon entropy.

The aim is to write a Python script that can:
* Efficiently process large compressed FASTQ files,
* Compute the Shannon entropy of the k-mer distribution,
* Detect when entropy estimation has converged, and
* Report and visualize the richness of the metagenome.

## Background
### What are metagenome studies?
A [metagenome](https://en.wikipedia.org/wiki/Metagenomics) is the combined DNA from all the microorganisms present in an environmental or biological sample (for example, soil, seawater, or the human gut).
Instead of isolating each species, scientists sequence all the DNA fragments together. The result is millions of short reads (100–150 bases each), each belonging to some microbe in the community.

Metagenomics allows us to:
* Discover what kinds of organisms are present,
* Measure community diversity,
* Identify new genes and metabolic pathways.

In this project, you will use one such dataset and infer community complexity by studying the sequence composition.


### What is a k-mer?
A [k-mer](https://en.wikipedia.org/wiki/K-mer) is a short DNA word of length k.
For example, if:

```
sequence = "ATGCG"
```

then the 3-mers are:

```
ATG, TGC, GCG
```

Each k-mer can be thought of as a "feature" describing local sequence composition.
Different species have distinct k-mer usage patterns, so the diversity of k-mers in your sample can reflect how many species contributed DNA.

### What is Shannon entropy?

[Shannon entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) is a measure of uncertainty or diversity in a set of elements.
It is defined as:

![](https://dl.dropboxusercontent.com/scl/fi/mzts977a53tg9gmi6qto7/pngpaste_3D8517B7-2B16-4001-B13B-02EA09D72318.png?rlkey=m0mjrjlli1bfosrb7xaftm1kz&dl=0)

where p<sub>i</sub> is the probability (frequency) of each unique k-mer.
* If all k-mers are equally frequent then the entropy is high (diverse).
* If only a few k-mers dominate, then entropy is low (less diverse).

In metagenomics, higher k-mer entropy suggests a more complex microbial community.

### Preliminary Tasks
1. Download a metagenomic FASTQ file
Go to the following link: https://www.ncbi.nlm.nih.gov/Traces/index.html?view=study&acc=ERP000108 Download one and only one file (any you want) that ends in `_clean.1.fq.gz` for example `MH0026_081224.clean.1.fq.gz`.

2. Do NOT decompress the file. Your Python script will read the compressed data directly.

3. Inspect the file. Run the following command in your terminal:

```bash
gunzip -c MH0026_081224.clean.1.fq.gz | head -n 10
```

You will see something like:

```
@I85_2_FC30MG0AAXX:5:1:3:1143/1
AGTACCTCTTAGTATTAAGCAACTCAAAGAGCTTTAGCATTTCTGGACGGACTTGTTCCAGATAATGCANTNTTN
+I85_2_FC30MG0AAXX:5:1:3:1143/1
hhhhhhhhhhhh`hhhhf^W`ZXhV[KJQMRLUNNWGGGONOLKENIJAGBAFTKEJD=AB@D=C<AEF;L;A=;
@I85_2_FC30MG0AAXX:5:1:3:697/1
CTTCTTCATCCTCTCGTTTGTAGTATCAGGATTCGTATTGTTATGGTACGGAAAGTAATTGTTCATCATNGTATN
+I85_2_FC30MG0AAXX:5:1:3:697/1
hhhhhhhhhhhhhhchhhhfaK\LL[XLHBHIWMCGDPYIPIEMIBCE@A?A<?=<=BD<AD@<<>>D=;AA?P;
@I85_2_FC30MG0AAXX:5:1:4:129/1
TGGCGGCCGTTCCATCGGCAAAGCCCTCCAGCGCATTCTTACAGAAATCATCGATCCTCTCGCTCTAATTATATN
```

Each read record has four lines:
* A header line starting with @ (read identifier)
* A DNA sequence line (the read itself)
* A + separator line
* A quality score line (ASCII characters encoding per-base confidence)

You will only use the sequence lines for this project.

### Implementation Tasks
#### Inputs
Your program should be a Python script that accepts:
* A required input FASTQ file (.fq.gz) like the one you downloaded 
* An optional k-mer size (k, integer 4–7)

Example usage:

```bash
python metagenome_entropy.py MH0026_081224.clean.1.fq.gz 6
```

If no `k` is given, the script should automatically run for k = 4, 5, 6, 7. (more on this on the Multi-k mode described later).

#### Parsing the FASTQ file
* Use Python’s gzip module to read the file without decompressing.
* Stream through the file (do not load all reads into memory). Use generators.
* Extract only the sequence lines (every second line in each 4-line record).
* For each sequence, generate all possible k-mers (e.g., for 6-mers, sliding window of size 6).

Skip k-mers containing ambiguous bases (`N`).

#### Computing Shannon entropy
As you process reads:
* Count occurrences of each unique k-mer using a dictionary or collections.Counter.
* Periodically (for example every 1000 reads), compute the Shannon entropy of the current distribution:

![](https://dl.dropboxusercontent.com/scl/fi/kuvx1zh2x6sd34m62lbhr/pngpaste_DCCE847F-18A3-4BB4-9C41-AF3F151342FB.png?rlkey=ce2xzwpo7y1h3q8zupvemkpsr&dl=0)

Continue reading reads until the entropy estimate converges, i.e.,

|H<sub>current</sub> - H<sub>previous</sub>| < 0.00001

Then stop processing and record:

1. The final entropy value
2. The number of reads processed before convergence
3. The total number of k-mers observed
4. The number of unique k-mers discovered

#### Visualization
After convergence:
* Generate a plot showing:
   * x-axis: Number of reads processed
   * y-axis: Number of unique k-mers discovered
* Save the plot as a PNG or display it on screen.

The curve should rise quickly and then plateau when most k-mers have been discovered. This reflects the richness and redundancy of your metagenome.

#### Multi-k mode
If no `k` argument is given:
* Run the algorithm for k = 4, 5, 6, 7
* For each k, record:
   * Converged Shannon entropy
   * Reads processed
   * Total k-mers observed

Print or save a summary table, for example:

| k | Shannon Entropy | Reads Processed | Total k-mers |
| - | --------------- | --------------- | ------------ |
| 4 | 6.12            | 45,000          | 270,000      |
| 5 | 8.45            | 62,000          | 372,000      |
| 6 | 9.77            | 79,000          | 474,000      |
| 7 | 10.13           | 98,000          | 588,000      |


### Tips
Use `gzip.open(filename, "rt")` to read compressed FASTQ files line-by-line.

