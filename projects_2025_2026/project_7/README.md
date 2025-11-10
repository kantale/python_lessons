

# Implementing and Evaluating Byte Pair Encoding (BPE) for DNA Tokenization

## Background
### What is String Tokenization in the Context of LLMs

Large Language Models (LLMs), such as GPT or BERT, process text not as raw characters but as tokens — meaningful chunks of text like words or subwords. The process of splitting text into these chunks is called tokenization.

Example:

```
Sentence: "Genomics is fascinating"
Tokens: ["Gen", "omics", "is", "fas", "cinating"]
```

Why tokenization matters:

* Reduces model vocabulary size (and memory usage)
* Enables models to generalize to unseen words
* Captures recurring language patterns and morphemes efficiently

In LLMs, good tokenization improves both efficiency and semantic representation.

### DNA Tokenization
DNA sequences are strings made of just four letters: A, C, G, T.
If we tokenize each character separately, every input to a model will be extremely long and lose biological context — the model will only see individual nucleotides, not biologically meaningful motifs.

Example:
| Representation | Tokens                    | Meaning                        |
| -------------- | ------------------------- | ------------------------------ |
| **Naive**      | A, C, G, T, A, C, G, T, … | Too fine-grained, no structure |
| **Better**     | ACGT, TATA, CGCG, …       | Captures biological motifs     |

In genomics, recurring patterns like promoters, repeats, or CpG islands often carry meaning.
Thus, we want tokenization methods that can learn frequent subsequences automatically rather than using fixed-length k-mers.

### Byte Pair Encoding (BPE) Tokenization
Byte Pair Encoding (BPE) is a subword tokenization algorithm that learns to combine frequently co-occurring symbols into new tokens.

How it works:
* Start with a vocabulary of single characters (`A`, `C`, `G`, `T`).
* Count all adjacent pairs (e.g., `AC`, `CG`, `GT`, ...).
* Merge the most frequent pair into a new token.
* Repeat until you reach a desired number of tokens (K).
* This way, BPE discovers frequent subsequences automatically — exactly what we need for DNA.

### Example of BPE Merging Steps
Let’s take the toy sequence:

```
ACGTACGTACGTA
```

Initial tokens: `A C G T A C G T A C G T A`

Step 1:
Most frequent pair: `C G --> CG`
--> Sequence becomes: `A CG T A CG T A CG T A`

Step 2:
Most frequent pair: `CG T --> CGT`
--> Sequence becomes: `A CGT A CGT A`

Step 3:
Most frequent pair: `A CGT --> ACGT`
--> Sequence becomes: `ACGT A ACGT A`

Final tokens: `{A, C, G, T, CG, GT, CGT, ACGT}`

## Project Data
You will work with chromosome 20 from the human reference genome (hg38).

Data source: Download from UCSC: https://hgdownload.cse.ucsc.edu/goldenpath/hg38/chromosomes/chr20.fa.gz

Preprocessing steps:
* Remove the first line (`>chr20`).
* Convert all lowercase letters (a,c,g,t) to uppercase (A,C,G,T).
* Merge all remaining lines into a single continuous sequence string.

After these steps, you will have a long DNA string representing the entire chromosome.


## Project Tasks
### PART 1 — Implement BPE Training
Implement a function that:
* Takes as input:
   * A DNA sequence (string)
   * The parameter K (maximum number of tokens)
* Returns:
   * The set of learned tokens, representing the trained BPE vocabulary

This is your **trained BPE**.

For example:
```python
def train_bpe(sequence, K):
    '''
    sequence: String
    K: int
    returns: set
    '''
    ...

```

### PART 2 — Implement DNA Tokenization

Implement a function that:
* Takes as input:
   * A DNA sequence
   * A trained BPE vocabulary (set of tokens)
* Returns:
   * A list of tokens representing the sequence

For example:
```python
def tokenize_dna(sequence, bpe_vocab):
    '''
    sequence: str
    bpe_vocab: int

    Returns: set
    '''
    ...

```

### PART 3 — Evaluate Tokenization Efficiency
Implement a method that:

1. Randomly selects a subsequence of length M from chromosome 20.
2. Trains a BPE model on it (train_bpe).
3. Selects another random subsequence of the same length M.
4. Tokenizes it using the trained BPE (tokenize_dna).
5. Records how many tokens were produced.
6. Repeats steps 1–5, 100 times with different random subsequences.
7. Reports the average number of tokens per sequence (i.e., average tokenization length).


### PART 4 — Explore Parameter Combinations
Run Part 3 for different combinations of:

| Parameter | Suggested Range             | Meaning                                                  |
| --------- | --------------------------- | -------------------------------------------------------- |
| **K**     | 10, 50, 100, 200, 500, 1000 | Number of tokens in the BPE vocabulary                   |
| **M**     | 1000, 5000, 10000, 50000    | Length of each subsequence used for training and testing |


For each combination, compute and report the average tokenized sequence length (as described in Part 3).

resent results in a table of the form:

| K   | M     | Average # of Tokens |
| --- | ----- | ------------------- |
| 10  | 1000  | ...                 |
| 10  | 5000  | ...                 |
| 50  | 10000 | ...                 |
| 500 | 50000 | ...                 |
| …   | …     | …                   |

## Additional Resources
* Wikipedia entry for BPE: https://en.wikipedia.org/wiki/Byte-pair_encoding
* Paper describing the algorihm (see Algorithm 1, Figure 5): 

> Ganesh Sapkota, Md Hasibur Rahman. Hybrid Tokenization Strategy for DNA Language Model using Byte Pair Encoding and K-MER Methods. arxviv. [link](https://arxiv.org/abs/2507.18570).  

* Paper using the algorithm and comparing it with other methods for DNA tokenization:

> LeAnn M Lindsey, Nicole L Pershing, Anisa Habib, Keith Dufault-Thompson, W Zac Stephens, Anne J Blaschke, Xiaofang Jiang, Hari Sundar, The impact of tokenizer selection in genomic language models, Bioinformatics, Volume 41, Issue 9, September 2025, btaf456, https://doi.org/10.1093/bioinformatics/btaf456

