## Project 3
This link http://purl.obolibrary.org/obo/mondo.json contains a json file with the [MONDO Disease ontology](https://obofoundry.org/ontology/mondo.html).

Practically this file contains a graph. 

* The nodes of the graph are under `data['graph'][0]['nodes']` if we assume that `data` is the object that contains the complete json file.
* The edges of the graph are under `data['graphs'][0]['edges']`

In this project we only care about the part of the graph for which the nodes have an `id` in the following format `http://purl.obolibrary.org/obo/MONDO_X`, where `X` is one or more numbers. 
These nodes contain a label under the `lbl` key. For example:

```json

{
      "id" : "http://purl.obolibrary.org/obo/MONDO_0000008",
      "lbl" : "obsolete bare lymphocyte syndrome",
      "type" : "CLASS",
}
```

We also the edges that have the following properties:

* the `sub` key contains a MONDO id
* the `obj` key contains a MONDO id
* The `pred` key is equal to `is_a`

For example:
```json
{
      "sub" : "http://purl.obolibrary.org/obo/MONDO_0013166", 
      "pred" : "is_a",
      "obj" : "http://purl.obolibrary.org/obo/MONDO_0017684",
      "meta" : {
        "basicPropertyValues" : [ {
          "pred" : "http://www.geneontology.org/formats/oboInOwl#source",
          "val" : "Orphanet:2066"
            } ]
        }
}
```
* Note: Ignore the `meta` key


The graph that these nodes and edges contain is a tree.


Create a function named `part_1` that will take as input parameter a path to this json file. The file should
* Create and return a python object that will hold the tree. Feel free to use anything (Class, dictionary, ...). Use only standard python libraries (no `pip instal ...`).

* Create a function `part_2` that will take as input the object returned from `part_1` and a MONDO ID without the URL part (for example `MONDO_0013166`). The function should return a list with the labels that exist in the 3rd level of the tree. Here are some real examples:

```python
mondo_tree = part_1('./data/mondo.json')

mondo_categories = part_2(mondo_tree, 'MONDO_0011719')
prints(mondo_categories)

# prints
# ['hereditary disease', 'cancer or benign tumor', 'digestive system disorder']
```

