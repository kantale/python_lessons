
# Project: Simulating Signal Transduction and Drug Response in ER+ Breast Cancer using Boolean Networks

## Background
Signal transduction networks in cancer determine how cells respond to growth signals, stress, or therapy. In ER+ (estrogen receptor-positive) breast cancer, several signaling pathways (such as PI3K/AKT, MAPK, and ER signaling) interact to regulate cell fate decisions like proliferation (growth) or apoptosis (programmed cell death).

A [Boolean network](https://en.wikipedia.org/wiki/Boolean_network) model simplifies these interactions:
* Each node (gene, protein, or process) can be ON (True) or OFF (False).
* Each node’s next state depends on logical rules describing its regulators.

For example:

```
AKT* = ((PIP3 or PIP3_2) and (PDK1_pm or mTORC2_pm) and not (Ipatasertib and not PIP3_2))
```

Here, `AKT` will be active if certain upstream signals are ON and not inhibited by the drug Ipatasertib.

## Tasks
### Tasks 1. Parse the model file

The file [breast_cancer.txt](breast_cancer.txt) contains Boolean rules in the format `Node* = expression`.

Parse each line into a Python dictionary like:

```python
rules = {
    "AKT": "((PIP3 or PIP3_2) and (PDK1_pm or mTORC2_pm) and not (Ipatasertib and not PIP3_2))",
    ...
}
```

#### Notes:
* You are free to use any other method for parsing / modelling the tree
* You can use [eval](https://docs.python.org/3/library/functions.html#eval) to parse the tree. Notice the WARNING in the page. 
* [Original source of the file](https://github.com/CASCI-lab/CANA/blob/master/cana/datasets/breast_cancer.txt)
* This file comes from this publication:

> Gómez Tejeda Zañudo J, Scaltriti M, Albert R. A network modeling approach to elucidate drug resistance mechanisms and predict combinatorial drug treatments in breast cancer. Cancer Converg. 2017;1(1):5. doi: 10.1186/s41236-017-0007-6. Epub 2017 Dec 29. PMID: 29623959; PMCID: PMC5876695.

### Task 2. Inspect the graph. 
Notice that some of the nodes are:
* Drug names: Fulvestrant, Alpelisib,  Everolimus, Trametinib, Ipatasertib, Palbociclib, Neratinib
* Roots. This means that they have no "parents". These are the genetic signature of the individual. Assume that these might have random states True or False at the beginning and that they do not change throughout the experiment
* Results: 
   * These are:
      * "Proliferation Nodes": Proliferation, Proliferation_2, Proliferation_3, Proliferation_4
      * "Apoptosis Nodes": Apoptosis, Apoptosis_2, Apoptosis_3, 
    * Obviously during treatment we want to maximimize the chances of Apoptosis (cancerous cells death) and minimize the chances of Apoptosis (cancerous cells proliferation). 
    * Assume that all result nodes are False (OFF) in all initial states. 


### Task 3. Run the model
Build a function that given a model and it's initial state, the function returns the next state of the model. The initial state should be:
* Drug names: All OFF except some random nodes that are ON (see later for this)
* Roots: Select Random ON or OFF
* Results: All OFF
* Rest Nodes: Select Random ON or OFF 

### Task 4. Run until..
Repeat Task 3 and keep each state in the memory. Run until the model enters in a state that has existed before.
When it finishes mark:

V = SUM(The number of "Apoptosis" nodes that are ON) - SUM(the number of "Proliferation" nodes that are ON).

### Task 5. Run for N=1 drug
* Initially run by having only one random drug ON and the rest OFF. 
* For each drug that is ON, run 1000 times (each time initialize differenty the state of the Rest Nodes) and measure the V value. 
* After the 1000 times run, report the AVERAGE(V) which the average V over the 1000 runs
* Report: Which Drug had the maximum AVERAGE(V) ?

### Task 6. Run for N=2 or more drugs
* Select by random N drugs to be ON and the rest to be OFF.
* Run the similar analysis as Task 5.
* Report which subset of drug with size=N has the maximum AVERAGE(V)

### Task 7. Run for N in range(2,8)
* Run Task 6 for all values of N from 1 to 7.
* Report which combination of initial Drugs that are ON, had the maximum AVERAGE(V)


### BONUS
* Allow both synchronous and asynchronous updates:
   * Synchronous: all nodes update at once.
   * Asynchronous: update one random node per iteration.

They can run the model from random initial states until a steady state (no change) or attractor is reached.
 
 
