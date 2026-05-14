---
title: "Geometry.Transform.BestFit()"
description: "Align the selected parts based on their geometric features."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Geometry > Transform > BestFit"
macro _link: "BestFitFunc"
---

## Description

Align the selected parts based on their geometric features.

## Syntax

```psj
Geometry.Transform.BestFit(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlStaticTarget`

- The target parts for the move operation.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlDynamicTarget`

- The parts to be moved.

<!-- @since:5.1.0 @type:Double @optional @default:0.00000001 -->
### `dError`

- The total difference in distance between nodes.

<!-- @since:5.1.0 @type:Integer @optional @default:400 -->
### `iMaxCycle`

- The number of iterations for the matrix calculation.

<!-- @since:5.1.0 @type:Integer @optional -->
### `iAlgorithmsType`

- The algorithms' type.
- It is set to 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {10-15}
# Prepare the model
Geometry.Part.Cube(
    dlLength=[0.003, 0.004, 0.005], 
    iPartColor=7463537)

Geometry.Part.Cube(
    dlLength=[0.004, 0.003, 0.005], 
    strName="Cube _2", iPartColor=15658599)

Geometry.Transform.BestFit(
    crlStaticTarget=[Part(1)], 
    crlDynamicTarget=[Part(2)], 
    dError=1e-08, 
    iMaxCycle=400, 
    iAlgorithmsType=0)
```
