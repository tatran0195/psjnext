---
title: "JPT.GetSelectedElemEdges()"
description: "Get all information of the selected edges"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get all information of the selected element edges.

## Syntax

```psj
JPT.GetSelectedElemEdges()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[DItemPairVector](../data-type/psj-utility/pre-utility/built-in-types/DItemPairVector)_ object or _List of [DItemPair](../data-type/psj-utility/pre-utility/built-in-types/DItemPair)_ objects containing information of the selected element edges under _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ format.

## Sample Code

```psj {6}
# Get the information of the selected element edges.
# This function returns a list of DItemPair objects or DItemPairVetor object storing
# information of element edges in DItem format
# Element edges are not actual entity but defined by connection of 2 nodes.

listSelElemEdges = JPT.GetSelectedElemEdges()
for i in listSelElemEdges:
    print ('1st Node: {}'.format(i.firstDItem.id))
    print ('2nd Node: {}'.format(i.secondDItem.id))
```
