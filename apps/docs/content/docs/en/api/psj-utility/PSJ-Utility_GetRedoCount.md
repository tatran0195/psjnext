---
title: "JPT.GetRedoCount()"
description: "Get the total number of redo action which is capable for executing"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the total number of Redo which is capable for executing.

## Syntax

```psj
JPT.GetRedoCount()
```

## Inputs

This utility function does not require any input value.

## Return Code

An _Integer_ specifying the number of Redo operation.

## Sample Code

```psj {12}
# Prepare model and redo steps
Geometry.Part.Cube(strName="Cube _11", iPartColor=11842649)
Geometry.Part.Cube(strName="Cube _12", iPartColor=14968422)
Geometry.Part.Cube(strName="Cube _13", iPartColor=6250447)
Geometry.Part.Cube(strName="Cube _14", iPartColor=12734402)
Geometry.Part.Cube(strName="Cube _15", iPartColor=16579696)
Geometry.Part.Cube(strName="Cube _16", iPartColor=7666683)
Geometry.Part.Cube(strName="Cube _17", iPartColor=12867524)
Toolbar.Undo(iCntUndo=3)

# Get the number of the available Redo
iRedoSteps = JPT.GetRedoCount()
JPT.Debugger(iRedoSteps) # Return an integer object with value = 3
```
