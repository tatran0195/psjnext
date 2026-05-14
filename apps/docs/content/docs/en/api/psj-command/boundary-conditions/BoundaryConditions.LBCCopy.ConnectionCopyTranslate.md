---
title: "BoundaryConditions.LBCCopy.ConnectionCopyTranslate()"
description: "Copy boundary conditions by using translation method"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LBCCopy > ConnectionCopyTranslate"
---

## Description

Copy boundary conditions by using translation method.

## Syntax

```psj
BoundaryConditions.LBCCopy.ConnectionCopyTranslate(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The connection copy method:
  - 0: Translation method. The copy destination is searched by translation in the X, Y, and Z directions.
  - 1: Rotation method. The copy destination is searched by the rotational movement of the specified axis.
  - 2: Mirror method. Search the copy destination by plane and offset amount. To define a plane, select 3 nodes or 2D elements.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMatchMethod`

- The match method:
  - 0: Node method. This matching method matches the exact nodes of the target to get matching results. It is useful when the target features are different.
  - 1: Feature method. This matching method is very fast, especially for large models, and requires face-to-face, vertex to vertex like feature matching.

<!-- @since:5.0.1 @type:List @optional @default:[0,0,0] -->
### `posVecTrans`

- The translational vector.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dMagnitude`

- The magnitude of the move distance of the copy destination.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTrandataDoffset`

- The trandata offset.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dTol`

- The tolerance value to be used for determination of conformity.
- Unit of length.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate system.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The list of targets.

## Return Code

A _Cursor_ specifying the created LBCs.

## Sample Code

```psj {11,12,13,14}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube _3", 
                   iPartColor=13259210)

BoundaryConditions.FixedConstraint(crlTargets=[Face(76)])

created _lbc = BoundaryConditions.LBCCopy.LBCCopyTranslate(posVecTrans=[-0.001, 0, 0], 
                                                          dMagnitude=0.03, 
                                                          dTol=0.1, 
                                                          crlTargets=[LbcConstraint(1)])

JPT.Debugger(created _lbc)
```
