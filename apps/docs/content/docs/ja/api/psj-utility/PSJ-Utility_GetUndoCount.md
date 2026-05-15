---
title: "JPT.GetUndoCount()"
description: "Get the total number of undo action which is capable for executing"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the total number of undo action which is capable of executing.

## Syntax

```psj
JPT.GetUndoCount()
```

## Inputs

This utility function does not require any input value.

## Return Code

An _Integer_ specifying the number of Undo operation.

## Sample Code

```psj {11}
# Prepare model and undo steps
Geometry.Part.Cube(strName="Cube _11", iPartColor=11842649)
Geometry.Part.Cube(strName="Cube _12", iPartColor=14968422)
Geometry.Part.Cube(strName="Cube _13", iPartColor=6250447)
Geometry.Part.Cube(strName="Cube _14", iPartColor=12734402)
Geometry.Part.Cube(strName="Cube _15", iPartColor=16579696)
Geometry.Part.Cube(strName="Cube _16", iPartColor=7666683)
Geometry.Part.Cube(strName="Cube _17", iPartColor=12867524)

# Get the number of the available Undo
iUndoSteps = JPT.GetUndoCount()
JPT.Debugger(iUndoSteps) # Return an integer object with value = 7
```
