---
title: "Connections.RigidElements.RBE2.ToCircleCenter()"
description: "create RBE2"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBE2 > ToCircleCenter"
---

## Description

Create RBE2

## Syntax

```psj
Connections.RigidElements.RBE2.ToCircleCenter(iMethod=19, crlMasterTargets=[], crlSlaveTargets=[], iEType=2, strName="RBE2 _1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:19 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlMasterTargets`

- The master target.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSlaveTargets`

- The slave target.

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `iEType`

- The e type.

<!-- @since:5.0.1 @type:String @optional @default:"RBE2 _1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoordSys`

- The coordinate system.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTolerance`

- The tolerance.

<!-- @since:5.0.1 @type:Integer @optional @default:63 -->
### `iUlDOFs`

- The ul d o fs.

<!-- @since:5.0.1 @type:Double List @optional @default:[0, 0, 0] -->
### `dlVirtualNodePos`

- The virtual node position.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSurfaceDef`

- The surface definition.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iEnableUpdateDispCS`

- The enable update displacement coordinate system.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableCornerOnly`

- The enable corner only.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iEnableCheckDuplicate`

- The enable check dulplicate.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDuplicateMode`

- The duplicate mode.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:1 -->
### `iEnableCheckDulplicate`

- The enable check dulplicate.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.RigidElements.RBE2.ToCircleCenter(iMethod=19, crlMasterTargets=[], crlSlaveTargets=[], iEType=2, strName="RBE2 _1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0)
```
