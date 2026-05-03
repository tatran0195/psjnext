---
title: "Geometry.Transform.BestFit()"
description: "Align the selected parts based on their geometric features."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Geometry > Transform > BestFit"
macro_link: "BestFitFunc"
---

## Description

Align the selected parts based on their geometric features.

## Syntax

```psj
Geometry.Transform.BestFit(...)
```

## Inputs

### `crlStaticTarget` @type(List\[Cursor]) @required

- The target parts for the move operation.

### `crlDynamicTarget` @type(List\[Cursor]) @required

- The parts to be moved.

### `dError` @type(Double) @default(0.00000001)

- The total difference in distance between nodes.

### `iMaxCycle` @type(Integer) @default(400)

- The number of iterations for the matrix calculation.

### `iAlgorithmsType` @type(Integer)

- The algorithms' type.
- It is set to 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{10-15}
# Prepare the model
Geometry.Part.Cube(
    dlLength=[0.003, 0.004, 0.005], 
    iPartColor=7463537)

Geometry.Part.Cube(
    dlLength=[0.004, 0.003, 0.005], 
    strName="Cube_2", iPartColor=15658599)

Geometry.Transform.BestFit(
    crlStaticTarget=[Part(1)], 
    crlDynamicTarget=[Part(2)], 
    dError=1e-08, 
    iMaxCycle=400, 
    iAlgorithmsType=0)
```
