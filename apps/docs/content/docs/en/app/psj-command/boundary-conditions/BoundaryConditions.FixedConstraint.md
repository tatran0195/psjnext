---
title: "BoundaryConditions.FixedConstraint()"
description: "Create a fixed constraint on selected Face, Edge or Node. User inputs the degree of freedom of fixed constraint and it will return a fixed constraint on selected items"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Boundary Conditions > Fixed Constraint"
---

## Description

Create a fixed constraint on selected Face, Edge or Node. User inputs the degree of freedom of fixed constraint and it will return a fixed constraint on selected items.

## Syntax

```psj
BoundaryConditions.FixedConstraint(...)
```

## Inputs

### `strName` @type(String) @default("Constraint1")

- The name of the fixed constraint to be created.

### `iDwDof` @type(Integer) @default(7)

- The degree of freedom (dof). This value is calculated by using OR operator between the following options:

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

### `iType` @type(Integer) @default(0)

- The type that is one of the following.
  - 0: None (do not use type)
  - 1: SUPPORT type.
  - 2: USET type.

### `iUsetType` @type(Integer) @default(0)

- The USET type. The USET type is only used when setting iType=2. The USET type is one of the following.
  - 0: U1
  - 1: U2
  - 2: U3
  - 3: U4
  - 4: U5
  - 5: U6

### `crTable` @type(Cursor) @default(None)

- The table of field data.

### `bAbaqusFixed` @type(Boolean) @default(False)

- To enable (_True_) or disable (_False_) the Abaqus fixed. This parameter is used for Abaqus I/F.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The list of targets for fixed constraint. This target can be Face, Edge or Node.

### `crEdit` @type(Cursor) @default(None)

- An existing fixed constraint. If this parameter is used, the specified fixed constraint will be modified. If it is lef&#x74;_&#x4E;one_, a new fixed constraint will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {2}
Geometry.Part.Cube()
creating_status = BoundaryConditions.FixedConstraint(crlTargets=[Face(26)])
JPT.Debugger(creating_status)
```
