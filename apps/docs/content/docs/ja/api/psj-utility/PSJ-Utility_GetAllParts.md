---
title: "JPT.GetAllParts()"
description: "Get all the information of all existing parts"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get all the information of all existing parts.

## Syntax

```psj
JPT.GetAllParts()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[BodyVector](../data-type/psj-utility/pre-utility/built-in-types/BodyVector)_ object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects containing all the information of all the existing parts.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2")
Geometry.Part.Cube(strName="Cube _3")
JPT.ViewFitToModel()

# Get the information of all existing parts
listDBodies = JPT.GetAllParts()
JPT.Debugger(listDBodies)

# Print all the related information of each existing part in list
for part in listDBodies:
    JPT.Debugger(part)
```
