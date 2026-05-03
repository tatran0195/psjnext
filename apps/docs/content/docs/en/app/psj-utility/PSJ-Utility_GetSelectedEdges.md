---
title: "JPT.GetSelectedEdges()"
description: "Get all information of the selected edges"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get all information of the selected edges.

## Syntax

```psj
JPT.GetSelectedEdges()
```

## Inputs

This utility function does not require any input value.

## Return Code

An _[EdgeVector](../data-type/psj-utility/pre-utility/built-in-types/EdgeVector)_ object or _List of [DEdge](../data-type/psj-utility/pre-utility/built-in-types/DEdge)_ objects containing all the information of the selected edges.

## Sample Code

```psj {13}
# Prepare model
Geometry.Part.Cube(iPartColor=7138156)
Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
Home.Find(strSearch="87 90 91 94 95 96 97 98", strSelectedType="Edge")
JPT.ViewFitToModel()

# Get the information of all selected edges
listSelEdges = JPT.GetSelectedEdges()
JPT.Debugger(listSelEdges)
JPT.Debugger(listSelEdges[3])
```
