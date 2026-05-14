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

<!-- @since:5.0.1 @type:String @optional @default:"Constraint1" -->
### `strName`

- The name of the fixed constraint to be created.

<!-- @since:5.0.1 @type:Integer @optional @default:7 -->
### `iDwDof`

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

<!-- @since:5.0.1 @type:Cursor @optional @default:None(global coordinate) -->
### `crCurCoord`

- The coordinate from which the fixed constraint is created.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The type that is one of the following.
  - 0: None (do not use type)
  - 1: SUPPORT type.
  - 2: USET type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iUsetType`

- The USET type. The USET type is only used when setting iType=2. The USET type is one of the following.
  - 0: U1
  - 1: U2
  - 2: U3
  - 3: U4
  - 4: U5
  - 5: U6

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTable`

- The table of field data.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bAbaqusFixed`

- The to enable (_True_) or disable (_False_) the Abaqus fixed. This parameter is used for Abaqus I/F.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The list of targets for fixed constraint. This target can be Face, Edge or Node.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing fixed constraint. If this parameter is used, the specified fixed constraint will be modified. If it is left _None_, a new fixed constraint will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {2}
Geometry.Part.Cube()
creating _status = BoundaryConditions.FixedConstraint(crlTargets=[Face(26)])
JPT.Debugger(creating _status)
```
