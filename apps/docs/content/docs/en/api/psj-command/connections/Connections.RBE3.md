---
title: "Connections.RBE3()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RBE3"
macro _link: "[Rbe3](../../macro/connections/Rbe3)"
---

## Description

Unknown Description

## Syntax

```psj
Connections.RBE3(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
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

<!-- @since:5.0.1 @type:Position @optional @default:[0, 0, 0] -->
### `posVirtualNodePos`

- The virtual node position.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSurfaceDef`

- The surface definition.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bUpdateDispCS`

- The update displacement coordinate system.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCornerOnly`

- The corner only.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.RBE3(iMethod=0, crlMasterTargets=[], crlSlaveTargets=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, posVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, bUpdateDispCS=True, bCornerOnly=False)
```
