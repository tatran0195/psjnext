---
title: "JPT.GetSelectedParts()"
description: "Get all information of the selected parts"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get all information of the selected parts.

## Syntax

```psj
JPT.GetSelectedParts()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[BodyVector](../data-type/psj-utility/pre-utility/built-in-types/BodyVector)_ object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects containing all the information of the selected parts.

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
Home.Find(strSearch="5 6 7 8", strSelectedType="Part")
JPT.ViewFitToModel()

# Get the information of all selected parts
listSelParts = JPT.GetSelectedParts()
JPT.Debugger(listSelParts)
JPT.Debugger(listSelParts[2])
```
