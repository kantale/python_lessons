# Drosophila Disease Model Analysis Project

## Introduction

This project focuses on analyzing disease model annotations that link Drosophila melanogaster genes to human diseases through the FlyBase database. Students will work with the FlyBase disease model annotations dataset (FB2025_02) to understand how model organisms like fruit flies are used to study human diseases. 

* Many genes are conserved between flies and humans (orthologs).
* Researchers can test gene mutations and interactions in flies that would be difficult in humans.
* The fly experiments help predict disease mechanisms relevant to humans.

## Task 1
Go to https://flybase.org/releases/FB2025_02/precomputed_files/human_disease/index.html and download the compressed TSV file [disease_model_annotations_fb_2025_02.tsv.gz](https://flybase.org/releases/FB2025_02/precomputed_files/human_disease/disease_model_annotations_fb_2025_02.tsv.gz)

**DO = Disease Ontology**

In this file you will notice that it has the following columns:
* `FBgn ID`. The ID of the Fly's gene. WE will ignore this
* `Gene symbol`. The symbol (or else name) of the Fly's gene. We will ignore this
* `HGNC ID`. The respective (ortholog) Human Gene (HGNC = Humman Genome Nomenclature Consortium). We will ignore it for this project.
* `DO qualifier`. How does this gene affects the human disease disribed in the `DO ID` column? Some examples:
   * "Exacerbates" means that modifying or mutating this Drosophila gene makes disease-like symptoms in the fly worse. For example, if a human disease is linked to gene X, researchers may mutate the orthologous fly gene and observe worsened disease-like phenotypes.
   * "Ameliorates" means that modifying or mutating this Drosophila gene makes disease-like symptoms in the fly better.
   * "Model of" means this Drosophila gene (often an ortholog of a human disease gene) can be used to study the disease in flies.

* `DO ID`. This is the ID of a human disease (DO = Disease Ontology) that this fly's gene can be used to model! Or else this human disease can be studied by studying the function of this fly's gene.
* `DO term`. The Disease Ontology name of the human disease
* Ignore the rest of the columns 


## Task 2
[Download](https://mondo.monarchinitiative.org/pages/download/) the mondo json file (available also [here](https://purl.obolibrary.org/obo/mondo.json)). For all `DO ID`s extract the relevant MONDO IDs. [Mondo](https://mondo.monarchinitiative.org/) is another disease ontology. The benefit of Mondo over DO is that Mondo is structured, meaning that each disease belongs to a category (for example Leukemia belongs to Cancer). See Project 3 for more on this. 

## Task 3
For all Mondo IDs identified in Task 2, extract all Mondo Categories as per the description of Project 3. 

## Task 4
For all different Mondo Categories and for all different `DO qualifiers` create a 2 X 2 respective [Contingency table](https://en.wikipedia.org/wiki/Contingency_table). Columns should be "Fly's gene Gene has this DO qualifier" and "FLy's gene Gene Does not have this DO qualifier". Rows should be "Fly's Gene has this Mondo Category" and "Fly's Gene Does not have this Mondo category".

## Task 5
For each contingency table compute the two-sided [fisher exact](https://en.wikipedia.org/wiki/Fisher%27s_exact_test) test. (Hint: Use `from scipy.stats import fisher_exact`). This will return the odds ratio and the pvalue of the test. 

## Task 6
Rank all p-values and print the top 10 lowest p-values. For each of the top-10 p-values print:
* The p-value
* The odds-ratio
* The Mondo Category
* The `DO qualifier`

## Bonus 1
* For each contingency table compute the expected value of the number of genes that has this mondo category and this DO qualifier under the assumption that these two are independent events. 
* Compute the fold_change as the ratio between the Observed count of "number of genes that has this mondo category and this DO qualifier" and the expected computed above
* Add these values to your report of the top-10 p-values

## Bonus 2
Apply multiple test correction by using `from statsmodels.stats.multitest import multipletests` with the following parameters:
* `alpha=0.05`
* `method='fdr_bh'`

Print all p-values for which the `multipletests` rejected the null hypothesis. 


