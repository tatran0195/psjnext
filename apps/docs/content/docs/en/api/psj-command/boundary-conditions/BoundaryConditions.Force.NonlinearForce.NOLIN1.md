---
title: "BoundaryConditions.Force.NonlinearForce.NOLIN1()"
description: "Create Nonlinear Force of NOLIN1(Table)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Force > NonlinearForce > NOLIN1"
---

## Description

Create Nonlinear Force of NOLIN1(Table).

## Syntax

```psj
BoundaryConditions.Force.NonlinearForce.NOLIN1(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"NonlinearForce1 _1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dForceScale`

- The force scale.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMomentScale`

- The moment scale.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iForcDir`

- The forc direction.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iForceDepends`

- The force depends.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMomentDir`

- The moment direction.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMomentDepends`

- The moment depends.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crForceTable`

- The force table.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMomentTable`

- The moment table.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlMaster`

- The master.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSlave`

- The slave.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Force.NonlinearForce.NOLIN1(strName="NonlinearForce1 _1", dForceScale=0.0, dMomentScale=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCoord=None, crForceTable=None, crMomentTable=None, crlMaster=[], crlSlave=[], crEdit=None)
```
