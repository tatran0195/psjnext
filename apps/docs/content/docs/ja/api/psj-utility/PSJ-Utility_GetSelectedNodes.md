---
title: "JPT.GetSelectedNodes()"
description: "Get all information of the selected nodes"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get all information of the selected nodes.

## Syntax

```psj
JPT.GetSelectedNodes()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[NodeVector](../data-type/psj-utility/pre-utility/built-in-types/NodeVector)_ object or _List of [DNode](../data-type/psj-utility/pre-utility/built-in-types/DNode)_ objects containing all the information of the selected nodes.

## Sample Code

```psj {13}
# Prepare model
Geometry.Part.Cube(iPartColor=7138156)
Geometry.Part.Cube(strName="Cube _2", iPartColor=5921475)
Geometry.Part.Cube(strName="Cube _3", iPartColor=6678117)
Geometry.Part.Cube(strName="Cube _4", iPartColor=11908427)
Geometry.Part.Cube(strName="Cube _5", iPartColor=15429611)
Geometry.Part.Cube(strName="Cube _6", iPartColor=7531634)
Geometry.Part.Cube(strName="Cube _7", iPartColor=12434775)
Home.Find(strSearch="20 21 22 23 24", strSelectedType="Node")
JPT.ViewFitToModel()

# Get the information of all selected nodes
listSelNodes = JPT.GetSelectedNodes()
JPT.Debugger(listSelNodes)
JPT.Debugger(listSelNodes[1])
```
