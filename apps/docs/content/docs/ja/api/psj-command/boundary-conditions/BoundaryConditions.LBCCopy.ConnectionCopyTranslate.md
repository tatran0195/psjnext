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

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the connection copy method:
  - 0: Translation method. The copy destination is searched by translation in the X, Y, and Z directions.
  - 1: Rotation method. The copy destination is searched by the rotational movement of the specified axis.
  - 2: Mirror method. Search the copy destination by plane and offset amount. To define a plane, select 3 nodes or 2D elements.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMatchMethod

- Specify the match method:
  - 0: Node method. This matching method matches the exact nodes of the target to get matching results. It is useful when the target features are different.
  - 1: Feature method. This matching method is very fast, especially for large models, and requires face-to-face, vertex to vertex like feature matching.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### posVecTrans

- Specify the translational vector.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### dMagnitude

- Specify the magnitude of the move distance of the copy destination.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### dTrandataDoffset

- Specify the trandata offset.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the tolerance value to be used for determination of conformity.
- Unit of length.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate system.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of targets.
- The default value is \[].

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
