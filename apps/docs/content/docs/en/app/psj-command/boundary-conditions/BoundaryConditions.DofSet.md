---
title: "BoundaryConditions.DofSet()"
description: "Create the degrees of freedom in the analysis set(ASET) in TS-Solver"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > DofSet"
---

## Description

Create the degrees of freedom in the analysis set(ASET) in TS-Solver.

## Syntax

```psj
BoundaryConditions.DofSet(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The list of the target(face/edge/node) for creating the ASET.

### `strName` @type(String) @default("DofSet1")

- The name of the ASET to be created.

### `iDwDof` @type(Integer) @default(7)

- The degree of freedom(DoF). This value is calculated by using OR operator between the following options:

  | Value | Option             |
  | ----- | ------------------ |
  | 1     | Ux (x translation) |
  | 2     | Uy (y translation) |
  | 4     | Uz (z translation) |
  | 8     | Rx (x rotation)    |
  | 16    | Ry (y rotation)    |
  | 32    | Rz (z rotation)    |

  - For example, if x, y, z translation must be constrained, then the iDwDof = 1 |2 |4 = 7.

### `crCurCoord` @type(Cursor) @default(None(global coordinate))

- The coordinate from which the fixed constraint is created.

### `crTable` @type(Cursor) @default(None)

- The table of field data.

### `crEdit` @type(Cursor) @default(None)

- An existing DoF Set. If this parameter is used, the specified DoF Set will be modified. If it is lef&#x74;_&#x4E;one_, a new DoF Set will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created_lbc = BoundaryConditions.DofSet(crlTargets=[Face(26)],
                                        strName="DofSet1",
                                        iDwDof=7)

JPT.Debugger(created_lbc)
```
