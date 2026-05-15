---
title: "BoundaryConditions.DofSet()"
description: "Create the degrees of freedom in the analysis set(ASET) in TS-Solver"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > DofSet"
---

## Description

Create the degrees of freedom in the analysis set(ASET) in TS-Solver.

## Syntax

```psj
BoundaryConditions.DofSet(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of the target(face/edge/node) for creating the ASET.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the ASET to be created.
- The default value is "DofSet1".

<!-- @since:5.0.1 @optional -->
### iDwDof

- Specify the degree of freedom(DoF). This value is calculated by using OR operator between the following options:

  | Value | Option             |
  | ----- | ------------------ |
  | 1     | Ux (x translation) |
  | 2     | Uy (y translation) |
  | 4     | Uz (z translation) |
  | 8     | Rx (x rotation)    |
  | 16    | Ry (y rotation)    |
  | 32    | Rz (z rotation)    |

  - For example, if x, y, z translation must be constrained, then the iDwDof = 1 |2 |4 = 7.

- The default value is 7.

<!-- @since:5.0.1 @optional -->
### crCurCoord

- Specify the coordinate from which the fixed constraint is created.
- The default value is _None_(global coordinate).

<!-- @since:5.0.1 @optional -->
### crTable

- Specify the table of field data.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing DoF Set. If this parameter is used, the specified DoF Set will be modified. If it is left _None_, a new DoF Set will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created _lbc = BoundaryConditions.DofSet(crlTargets=[Face(26)],
                                        strName="DofSet1",
                                        iDwDof=7)

JPT.Debugger(created _lbc)
```
