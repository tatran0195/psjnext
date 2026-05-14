---
title: "JPT.GetSelectedFaces()"
description: "Get all information of the selected faces"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get all information of the selected faces.

## Syntax

```psj
JPT.GetSelectedFaces()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[FaceVector](../data-type/psj-utility/pre-utility/built-in-types/FaceVector)_ object or _List of [DFace](../data-type/psj-utility/pre-utility/built-in-types/DFace)_ objects containing all the information of the selected faces.

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
Home.Find(strSearch="20 21 22 23 24", strSelectedType="Face")
JPT.ViewFitToModel()

# Get the information of all selected edges
listSelFaces = JPT.GetSelectedFaces()
JPT.Debugger(listSelFaces)
JPT.Debugger(listSelFaces[2])
```
