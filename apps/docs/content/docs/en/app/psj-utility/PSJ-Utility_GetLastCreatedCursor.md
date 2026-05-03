---
title: "JPT.GetLastCreatedCursor()"
description: "Get the information of the last created entity"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get the information of the last created entity.

## Syntax

```psj
JPT.GetLastCreatedCursor()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing the information of the last created object.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of the last created part
lastCreatedCursor = JPT.GetLastCreatedCursor()
JPT.Debugger(lastCreatedCursor[0]) # Cube_3
```
