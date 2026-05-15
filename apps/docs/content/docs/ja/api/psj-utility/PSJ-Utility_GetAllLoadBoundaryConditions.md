---
title: "JPT.GetAllLoadBoundaryConditions()"
description: "Get all the information of all existing loads and boundary conditions"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get all the information of all existing loads and boundary conditions.

## Syntax

```psj
JPT.GetAllLoadBoundaryConditions()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[LoadBCVector](../data-type/psj-utility/pre-utility/built-in-types/LoadBCVector)_ object or _List of [DLoadBC](../data-type/psj-utility/pre-utility/built-in-types/DLoadBC)_ objects containing all the information of all the existing loads and boundary conditions.

## Sample Code

```psj {10}
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube _2", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.024, 0.0, 0.0], strName="Cube _3", iPartColor=7697908)
BoundaryConditions.FixedConstraint(crlTargets=[Face(76)])
BoundaryConditions.Pressure.General(crlTargets=[Face(52)])
JPT.ViewFitToModel()

# Get the information of all existing loads and boundary conditions
listDLoadBCs = JPT.GetAllLoadBoundaryConditions()
JPT.Debugger(listDLoadBCs)

# Print all the related information of each existing load/boundary condition in list
for lbc in listDLoadBCs:
    JPT.Debugger(lbc)
```
