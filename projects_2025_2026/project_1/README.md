# Drug-Drug Interaction (DDI) Prediction Exercise

## What are DDIs?

Drug-Drug Interactions (DDIs) occur when two or more drugs are taken together and one drug affects the activity, efficacy, or safety of another. For example, one drug might increase the side effects of another, or decrease its effectiveness. Understanding DDIs is crucial for patient safety, as adverse drug interactions can lead to serious health complications.

In this project, we work with a dataset containing known drug-drug interactions from DrugBank, where each interaction is labeled with a specific type of pharmacological effect (relation type). There are 86 different relation types (IDs 0-85), each describing a specific way drugs can interact, such as:
- "Drug1 may increase the anticoagulant activities of Drug2" (relation ID 5)
- "The risk or severity of adverse effects can be increased when Drug1 is combined with Drug2" (relation ID 48)
- "The metabolism of Drug2 can be decreased when combined with Drug1" (relation ID 46)

## Project Overview

This exercise implements a k-nearest neighbor ([k-NN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)) based approach to predict drug-drug interaction types. The core idea is that similar drug pairs (based on their molecular structure) are likely to have similar interaction types. For each test drug pair, we find the most similar training drug pair and predict the same interaction type. 

For this project you can use k=1 (easier) but you are free to experiment with larger values of k. 

## Project setup 
For this project you will need a list of files from the [DDI-Bench](https://github.com/LARS-research/DDI-Bench) repository that accompamies the pubication

> Zhenqian Shen, Mingyang Zhou, Yongqi Zhang, Quanming Yao, Benchmarking drug–drug interaction prediction methods: a perspective of distribution changes, Bioinformatics, Volume 41, Issue 11, November 2025, btaf569, https://doi.org/10.1093/bioinformatics/btaf569

You can either clone the repository or (if you don't know what that is) you can [download it as a zip file](https://github.com/LARS-research/DDI-Bench/archive/refs/heads/main.zip)  


## Data Semantics

### Training and Test Files

The project uses two main data files:

1. Training file (`DDI_Ben/DDI_Ben/data/drugbank_random/train.txt`): Contains known drug-drug interactions used to learn patterns. Each line has the format:
   ```
   drug_id_a drug_id_b relation_id
   ```
   - `drug_id_a` and `drug_id_b`: Integer identifiers for the two drugs in the interaction
   - `relation_id`: Integer (0-85) representing the type of interaction between the two drugs

2. Test file (`DDI_Ben/DDI_Ben/data/drugbank_random/test_S0.txt`): Contains drug-drug interactions for evaluation. Uses the same format as the training file.

### Why Use Training and Testing Files?

The separation of training and testing data is fundamental to machine learning:

- Training data: Used to "learn" patterns. In our k-NN approach, we use it as a reference database to find similar drug pairs.
- Test data: Used to evaluate how well our method generalizes to new, unseen drug pairs. We never use test data during training to get an honest assessment of performance.

This separation helps ensure that our predictions work on real-world scenarios where we encounter new drug combinations that weren't in our training set.

### Relations file 

The `relation2id.json` file maps relation IDs (as strings) to their textual descriptions, e.g., `"48": "The risk or severity of adverse effects can be increased when #Drug1 is combined with #Drug2."` 

Basically it contains the name of the relation that exist in the third column of the train and test files. It contains a dictionary. Keys are integer values that are used in train and test files. Values are the name of the relationship. 

You can open this file with:
```python
import json

with open('DDI_Ben/TextDDI/data/drugbank_random/relation2id.json') as f:
    data = json.load(f)

```

### Molecular Features File

The file `DDI_Ben/DDI_Ben/data/initial/drugbank/DB_molecular_feats.pkl` contains precomputed molecular features for each drug:

-Morgan_Features: Binary fingerprint vectors (0s and 1s) representing molecular substructures. These are computed using RDKit's Morgan circular fingerprints (for more info [check this](https://www.rdkit.org/UGM/2012/Landrum_RDKit_UGM.Fingerprints.Final.pptx.pdf), although you don't need any more info for the project). Drugs with similar chemical structures will have similar Morgan fingerprints. The Tanimoto distance (also called [Jaccard distance](https://en.wikipedia.org/wiki/Jaccard_index)) is commonly used to measure similarity between these binary fingerprints.

- RDKit2D_Features: Continuous numerical vectors containing 2D physicochemical descriptors computed by [RDKit](https://www.rdkit.org/). These capture properties like molecular weight, lipophilicity (logP), polar surface area, number of aromatic rings, and many other molecular properties. These features are normalized and ready to use. [Cosine distance](https://en.wikipedia.org/wiki/Cosine_similarity) is appropriate for measuring similarity between these continuous feature vectors.

The [pickle file](https://docs.python.org/3/library/pickle.html) structure:
```python
{
    'DrugBank ID': [...],      # DrugBank identifiers
    'Node ID': [...],          # Integer node IDs used in the interaction files
    'SMILES': [...],           # SMILES string representations
    'Morgan_Features': [...],  # Binary fingerprint arrays
    'RDKit2D_Features': [...]  # Continuous descriptor arrays
}
```

To "unpickle" the file use the following code:
```python
import picle

with open('DDI_Ben/DDI_Ben/data/initial/drugbank/DB_molecular_feats.pkl', 'rb') as f:
    data = pickle.load(f)

print(data.keys()) # 
```

Important:
* Always use `'rb'` (read binary) mode when opening pickle files, as they contain binary data.
* All lists have the same length (1,710 drugs) and are aligned by index.
* The `Node ID` list can be used to map the Molecular Features Files (DB_molecular_feats.pkl) with the train and test file. 


## Algorithm Description

The implementation uses a nearest neighbor classifier:

1. For each test drug pair (drug_a, drug_b) with unknown relation type:
   - Extract molecular features for both drugs (Morgan and RDKit2D features)
   
2. Compare with all training pairs:
   - For each training pair (train_a, train_b) with known relation type:
     - Compute Tanimoto distance between Morgan features of test_a and train_a
     - Compute Tanimoto distance between Morgan features of test_b and train_b
     - Average these to get Morgan feature distance: `mf_distance = (from_tanimoto + to_tanimoto) / 2`
     
     - Compute cosine distance between RDKit2D features of test_a and train_a
     - Compute cosine distance between RDKit2D features of test_b and train_b
     - Average these to get RDKit2D feature distance: `rd_distance = (from_cosine + to_cosine) / 2`
     
     - Combine both distances with weights: `total_distance = mf_weight * mf_distance + rd_weight * rd_distance`
      - In my implementation I used `mf_weight=0.5` and `rd_weight=0.5` but you are free to experiment!
     - Track the training pair with the minimum total distance

3. Predict: 
  - If k=1, assign the relation type of the most similar training pair to the test pair. 
  - If you use k>1 then you should keep all k shortest distances and assign the relation type to the one that has the maximum representation in all k shortest distances. For example if k=5 and the shortest maximum distances have class values 7,3,7,7,1 then you will assign it to relation type "7".  

4. Evaluate: Compare predicted relation type with the true relation type from the test file. If the prediction was correct then `number_of_correct_predictions += 1`

## Accuracy Calculation

The accuracy is computed as:

```
accuracy = number_of_correct_predictions / total number of test samples
```

Where a prediction is "correct" if the predicted `relation_id` exactly matches the true `relation_id` from the test file.

This is a multi-class classification problem with 86 possible classes (relation types 0-85). The accuracy metric tells us what fraction of test drug pairs we correctly classified.

## Performance Note

Important: The current implementation compares each test sample against all training samples, which is computationally expensive. For the full test set (12,411 samples) compared against the full training set (99,283 samples), this requires over 1.2 billion distance calculations, which can take many hours to complete.

Therefore, the implementation includes a `cutoff` parameter that limits the number of test samples processed. For example, `cutoff=20` processes only the first 20 test samples, which is useful for:
- Quick testing and debugging
- Understanding the algorithm behavior
- Initial development and validation

You are free to apply any optimization that you think is relevant (by pre-computing feature matrices, using vectorized operations, or implementing more efficient data structures). 

## Inference 
Your code should be able to compute the name of the relation type between any two DrugBank IDs. 

## Suggested Command Line Arguments

The implementation supports two modes: **train** (for evaluation) and **inference** (for prediction).

### Required Arguments (All Modes)

- `--molecular_feats`: Path to the molecular features pickle file (e.g., `DDI_Ben/DDI_Ben/data/initial/drugbank/DB_molecular_feats.pkl`)
- `--relation2id`: Path to the relation ID mapping JSON file (e.g., `DDI_Ben/TextDDI/data/drugbank_random/relation2id.json`)
- `--train`: Path to the training data file (e.g., `DDI_Ben/DDI_Ben/data/drugbank_random/train.txt`)
- `--mode`: Operation mode, must be either `train` or `inference`

### Optional Arguments

- `--test`: Path to the test data file (e.g., `DDI_Ben/DDI_Ben/data/drugbank_random/test_S0.txt`)
  - **Required when `--mode train`**, optional for inference mode
- `--cutoff`: Integer specifying the maximum number of test samples to process (useful for quick testing/debugging)
  - If not specified, all test samples will be processed
- `--drugbank_1`: First DrugBank ID (e.g., `DB13231`)
  - **Required when `--mode inference`**
- `--drugbank_2`: Second DrugBank ID (e.g., `DB00244`)
  - **Required when `--mode inference`**

### Example Commands

#### Train Mode (Evaluation)

Evaluate the model on test data:

```bash
python implementation.py \
    --molecular_feats DDI_Ben/DDI_Ben/data/initial/drugbank/DB_molecular_feats.pkl \
    --train DDI_Ben/DDI_Ben/data/drugbank_random/train.txt \
    --test DDI_Ben/DDI_Ben/data/drugbank_random/test_S0.txt \
    --cutoff 20 \
    --mode train
```

Example output (from my implementation):
```
Sample: 1/12411, Predicted: 48, Real: 48
Sample: 2/12411, Predicted: 72, Real: 72
Sample: 3/12411, Predicted: 66, Real: 66
Sample: 4/12411, Predicted: 48, Real: 48
Sample: 5/12411, Predicted: 48, Real: 48
Sample: 6/12411, Predicted: 48, Real: 1
Sample: 7/12411, Predicted: 48, Real: 48
Sample: 8/12411, Predicted: 66, Real: 66
Sample: 9/12411, Predicted: 1, Real: 1
Sample: 10/12411, Predicted: 46, Real: 48
Sample: 11/12411, Predicted: 48, Real: 1
Sample: 12/12411, Predicted: 66, Real: 66
Sample: 13/12411, Predicted: 66, Real: 66
Sample: 14/12411, Predicted: 48, Real: 48
Sample: 15/12411, Predicted: 66, Real: 66
Sample: 16/12411, Predicted: 48, Real: 48
Sample: 17/12411, Predicted: 72, Real: 72
Sample: 18/12411, Predicted: 74, Real: 72
Sample: 19/12411, Predicted: 48, Real: 48
Sample: 20/12411, Predicted: 1, Real: 1
Total: 20, correct: 16  wrong: 4
Accuracy: 0.8
```

#### Inference Mode (Prediction)

Predict the interaction type between two specific drugs:

```bash
python implementation.py \
    --molecular_feats DDI_Ben/DDI_Ben/data/initial/drugbank/DB_molecular_feats.pkl \
    --relation2id DDI_Ben/TextDDI/data/drugbank_random/relation2id.json \
    --train DDI_Ben/DDI_Ben/data/drugbank_random/train.txt \
    --mode inference \
    --drugbank_1 DB13231 \
    --drugbank_2 DB00244
```

Note: In inference mode, the `--test` argument is not required since we're predicting for specific DrugBank IDs rather than evaluating on a test set.

Example output:
```
Prediction: The therapeutic efficacy of #Drug2 can be decreased when used in combination with #Drug1.
```



