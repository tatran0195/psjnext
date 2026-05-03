---
title: "BoundaryConditions.LBCCopy.ConnectionCopyTranslate()"
description: "Copy boundary conditions by using translation method"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > LBCCopy > ConnectionCopyTranslate"
---

## Description

Copy boundary conditions by using translation method.

## Syntax

```psj
BoundaryConditions.LBCCopy.ConnectionCopyTranslate(...)
```

## Inputs

### `iMethod` @type(Integer) @default(0)

- The connection copy method:
  - 0: Translation method. The copy destination is searched by translation in the X, Y, and Z directions.
  - 1: Rotation method. The copy destination is searched by the rotational movement of the specified axis.
  - 2: Mirror method. Search the copy destination by plane and offset amount. To define a plane, select 3 nodes or 2D elements.

### `iMatchMethod` @type(Integer) @default(0)

- The match method:
  - 0: Node method. This matching method matches the exact nodes of the target to get matching results. It is useful when the target features are different.
  - 1: Feature method. This matching method is very fast, especially for large models, and requires face-to-face, vertex to vertex like feature matching.

### `posVecTrans` @type(List) @default(\[0,0,0])

- The translational vector.

### `dMagnitude` @type(Double) @default(1.0)

- The magnitude of the move distance of the copy destination.

### `dTrandataDoffset` @type(Double) @default(0.0)

- The trandata offset.

### `dTol` @type(Double) @default(1.0)

- The tolerance value to be used for determination of conformity.
- Unit of length.

### `crCoord` @type(Cursor) @default(None)

- The coordinate system.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The list of targets.

## Return Code

A _Cursor_ specifying the created LBCs.

## Sample Code

```psj {11,12,13,14}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_3", 
                   iPartColor=13259210)

BoundaryConditions.FixedConstraint(crlTargets=[Face(76)])

created_lbc = BoundaryConditions.LBCCopy.LBCCopyTranslate(posVecTrans=[-0.001, 0, 0], 
                                                          dMagnitude=0.03, 
                                                          dTol=0.1, 
                                                          crlTargets=[LbcConstraint(1)])

JPT.Debugger(created_lbc)
```
