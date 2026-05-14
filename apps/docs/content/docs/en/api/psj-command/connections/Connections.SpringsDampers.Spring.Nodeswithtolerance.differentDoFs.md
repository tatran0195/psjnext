---
title: "Connections.SpringsDampers.Spring.Nodeswithtolerance.differentDoFs()"
description: "Spring connection Nodes with tolerance different DOFs"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > SpringsDampers > Spring > Nodeswithtolerance > differentDoFs"
---

## Description

Spring connection Nodes with tolerance different DOFs

## Syntax

```psj
Connections.SpringsDampers.Spring.Nodeswithtolerance.differentDoFs(iMethod=0, strName="SPRING", crlMasterTargets=[], crlSlaveTargets=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT _DBL, dStressCoef=DFLT _DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:String @optional @default:"SPRING" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlMasterTargets`

- The master target.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSlaveTargets`

- The slave target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoordSys`

- The coordinate system.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSpringType`

- The spring type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iGround`

- The ground.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTolerance`

- The tolerance.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDirection`

- The direction.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDistributeMode`

- The distribute mode.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDof1`

- The dof1.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDof2`

- The dof2.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDampCoef`

- The damp coefficient .

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dStressCoef`

- The stress coefficient .

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posTStiffness`

- The t stiffness.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posRStiffness`

- The r stiffness.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bUpdateDispCS`

- The update displacement coordinate system.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.SpringsDampers.Spring.Nodeswithtolerance.differentDoFs(iMethod=0, strName="SPRING", crlMasterTargets=[], crlSlaveTargets=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT _DBL, dStressCoef=DFLT _DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None)
```
