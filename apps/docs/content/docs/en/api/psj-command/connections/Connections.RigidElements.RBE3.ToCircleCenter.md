---
title: "Connections.RigidElements.RBE3.ToCircleCenter()"
description: "Create RBE3"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBE3 > ToCircleCenter"
---

## Description

Create RBE3

## Syntax

```psj
Connections.RigidElements.RBE3.ToCircleCenter(iMethod=19, crlMasterTargets=[], crlSlaveTargets=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False)
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

<!-- @since:5.0.1 @type:RBE3TERM _CONNECTION List @optional @default:[] -->
### `listRbe3TermConnection`

- The rbe3 term connection.

<!-- @since:5.0.1 @type:Integer @optional @default:3 -->
### `iTypeRBE3`

- The type r e3.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoordSys`

- The coordinate system.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTolerance`

- The tolerance.

<!-- @since:5.0.1 @type:Double List @optional @default:[0, 0, 0] -->
### `dlVirtualNodePos`

- The virtual node position.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSurfaceDef`

- The surface definition.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Integer @optional @default:True -->
### `iEnableUpdateDispCS`

- The enable update displacement coordinate system.

<!-- @since:5.0.1 @type:Integer @optional @default:False -->
### `iEnableCornerOnly`

- The enable corner only.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.RigidElements.RBE3.ToCircleCenter(iMethod=19, crlMasterTargets=[], crlSlaveTargets=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False)
```
