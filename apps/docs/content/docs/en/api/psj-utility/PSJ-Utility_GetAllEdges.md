---
title: "JPT.GetAllEdges()"
description: "Get all the information of all existing edges"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get all the information of all existing edges.

## Syntax

```psj
JPT.GetAllEdges()
```

## Inputs

This utility function does not require any input value.

## Return Code

An _[EdgeVector](../data-type/psj-utility/pre-utility/built-in-types/EdgeVector)_ object or _List of [DEdge](../data-type/psj-utility/pre-utility/built-in-types/DEdge)_ objects containing all the information of all the existing edges.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2")
Geometry.Part.Cube(strName="Cube _3")
JPT.ViewFitToModel()

# Get the information of all existing edges
listDEdges = JPT.GetAllEdges()
JPT.Debugger(listDEdges)

# Print all the related information of each existing edge in list
for edge in listDEdges:
    JPT.Debugger(edge)
```
