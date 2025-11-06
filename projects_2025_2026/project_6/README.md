

# Polypharmacy side-effect association network
The [Polypharmacy side-effect association network](https://snap.stanford.edu/biodata/datasets/10017/10017-ChChSe-Decagon.html) is part of the [SNAP](https://snap.stanford.edu/index.html) (Stanford Network Analysis Project) project. 

The dataset contains a graph where each node connects two drugs. Each edge denotes that these drugs are likely to develop a side effect when prescribed together (a phenomenon called polypharmacy, or [concomitant drugs](https://en.wikipedia.org/wiki/Concomitant_drug)).

You can download the the network in the form of a compressed CSV file from this link: [ChChSe-Decagon_polypharmacy.csv.gz](https://snap.stanford.edu/biodata/datasets/10017/files/ChChSe-Decagon_polypharmacy.csv.gz). 

Let's see what is happening in this file:
```bash
gunzip -c ChChSe-Decagon_polypharmacy.csv.gz | head -n 10
```

```
# STITCH 1,STITCH 2,Polypharmacy Side Effect,Side Effect Name
CID000002173,CID000003345,C0151714,hypermagnesemia
CID000002173,CID000003345,C0035344,retinopathy of prematurity
CID000002173,CID000003345,C0004144,atelectasis
CID000002173,CID000003345,C0002063,alkalosis
CID000002173,CID000003345,C0004604,Back Ache
CID000002173,CID000003345,C0034063,lung edema
CID000002173,CID000003345,C0085631,agitated
CID000002173,CID000003345,C0013384,abnormal movements
CID000002173,CID000003345,C0001122,Acidosis
```

The columns are:
* `STITCH 1` . This is the ID Drug 1 in [STITCH Ontology](https://stitch-db.org/)
* `STITCH 2` . This is the ID Drug 2 in STITCH Ontology
* `Polypharmacy Side Effect`. This is the ID of the disease / side effect in the [MedGen database](https://www.ncbi.nlm.nih.gov/medgen/)
* `Side Effect Name`. The name of the disease. 

For example the line:
```
CID000002173,CID000003345,C0151714,hypermagnesemia
```

means that when drugs CID000002173, CID000003345 are prescribed together then there is an elavated risk of developing hypermagnesemia. 

Of course we can model the complete dataset as a graph, where each link is an edge. 

In [graph theory](https://en.wikipedia.org/wiki/Graph_theory) there is the concept of [Connected Component](https://en.wikipedia.org/wiki/Component_(graph_theory)). A connected component is a subset of a graph that satisfies the following attributes:
* There is a path from any node to any other node within the component. 
* There is no path between a node in a component and another node in another component. 

Wikipedia has this very educational example:

![](https://dl.dropboxusercontent.com/scl/fi/s87kpk9xf7r1408p7c08y/pngpaste_29FC4A03-7233-4ADC-8A17-32493F8FCA03.png?rlkey=clky5281rrm905b80jgktfll1&dl=0)

This is a graph with 3 connected components. 

Now let's go back to our polypharmacy dataset. For each different side effect we can generate a different graph that contains only the edges that have this disease. For example these are the first 5 nodes of the `atelectasis` graph.

```bash
gunzip -c ChChSe-Decagon_polypharmacy.csv.gz | grep atelectasis | head -n 5
CID000002173,CID000003345,C0004144,atelectasis
CID000001302,CID000005064,C0004144,atelectasis
CID000004212,CID000060953,C0004144,atelectasis
CID000002907,CID000003345,C0004144,atelectasis
CID000000838,CID000002617,C0004144,atelectasis
```

If we use all atelectasis edges (and not just the first 5) we can generate the graph of the atelectasis disease. This graph will have it's own sets of connected components. There is another graph for alkalosis, another for hypermagnesemia, and so on.

In this project you will have to write code to answer the following simple question:

**Of all the diseases whose graphs have only one connected component, which one (disease) has the largest component?**

## Important Requirements and Notes
* Do not load the complete graph in memory (useless waste of resources). This can be solved with a **single** read (parsing) of the CSV file. 
* Think of using a suitable data structure
* Do not use networkx or any other external library. Getting the connected components is a simple problem..
* My implementation takes ~10 seconds. 

## Bonus 
* For each disease print the number of connected components and their average size. For example if a disease has 3 connected components each having 10, 12 and 5 nodes, the average size is 9.


