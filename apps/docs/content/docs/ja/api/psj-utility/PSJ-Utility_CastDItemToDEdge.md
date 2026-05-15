---
title: "JPT.CastDItemToDEdge()"
description: "Convert DItem object to DEdge object"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DEdge](../data-type/psj-utility/pre-utility/built-in-types/DEdge)_ object to get the information of the selected edge.

## Syntax

```psj
JPT.CastDItemToDEdge(DItemObject)
```

## Inputs

### `DItemObject`

- A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.

## Return Code

A _[DEdge](../data-type/psj-utility/pre-utility/built-in-types/DEdge)_ object (Edge with relating information).

## Sample Code

```psj {11}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get Edge object as DItem object from the created list of DItem objects
listDItemEdges = JPT.GetAllByTypeID(JPT.DItemType.EDGE)
dItemEdge = listDItemEdges[0]
JPT.Debugger(dItemEdge)

# Convert from the above DItem object to DEdge object
dEdge = JPT.CastDItemToDEdge(dItemEdge)
JPT.Debugger(dEdge)
```
