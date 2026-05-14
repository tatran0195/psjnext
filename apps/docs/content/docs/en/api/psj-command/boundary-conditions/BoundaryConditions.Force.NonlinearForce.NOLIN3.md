---
title: "BoundaryConditions.Force.NonlinearForce.NOLIN3()"
description: "create nonlinear force NOLIN3"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Force > NonlinearForce > NOLIN3"
---

## Description

Create nonlinear force NOLIN3.

## Syntax

```psj
BoundaryConditions.Force.NonlinearForce.NOLIN3(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dForceScale`

- The force scale.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMomentScale`

- The moment scale.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dForcePowerA`

- The force power a.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMomentPowerA`

- The moment power a.

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
### `crCurCoord`

- The cur coordinate.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlMasterTargets`

- The master target.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSlaveTargets`

- The slave target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Force.NonlinearForce.NOLIN3(strName, dForceScale=0.0, dMomentScale=0.0, dForcePowerA=0.0, dMomentPowerA=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCurCoord=None, crlMasterTargets=[], crlSlaveTargets=[], crEdit=None)
```
