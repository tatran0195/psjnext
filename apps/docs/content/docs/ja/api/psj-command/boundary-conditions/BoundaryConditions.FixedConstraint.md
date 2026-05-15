---
title: "BoundaryConditions.FixedConstraint()"
description: "Create a fixed constraint on selected Face, Edge or Node. User inputs the degree of freedom of fixed constraint and it will return a fixed constraint on selected items"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Boundary Conditions > Fixed Constraint"
---

## Description

Create a fixed constraint on selected Face, Edge or Node. User inputs the degree of freedom of fixed constraint and it will return a fixed constraint on selected items.

## Syntax

```psj
BoundaryConditions.FixedConstraint(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the fixed constraint to be created.
- The default value is "Constraint1".

<!-- @since:5.0.1 @optional -->
### iDwDof

- Specify the degree of freedom (dof). This value is calculated by using OR operator between the following options:

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
### iType

- Specify the type that is one of the following.
  - 0: None (do not use type)
  - 1: SUPPORT type.
  - 2: USET type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iUsetType

- Specify the USET type. The USET type is only used when setting iType=2. The USET type is one of the following.
  - 0: U1
  - 1: U2
  - 2: U3
  - 3: U4
  - 4: U5
  - 5: U6
- The default value is 0

<!-- @since:5.0.1 @optional -->
### crTable

- Specify the table of field data.
- The default value is _None_.

### `bAbaqusFixed`

- A _Boolean_ to enable (_True_) or disable (_False_) the Abaqus fixed. This parameter is used for Abaqus I/F.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of targets for fixed constraint. This target can be Face, Edge or Node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing fixed constraint. If this parameter is used, the specified fixed constraint will be modified. If it is left _None_, a new fixed constraint will be created.
- The default value is None.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {2}
Geometry.Part.Cube()
creating _status = BoundaryConditions.FixedConstraint(crlTargets=[Face(26)])
JPT.Debugger(creating _status)
```
