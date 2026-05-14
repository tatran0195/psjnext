---
title: "Connections.RigidElements.RBE3.OneToOne()"
description: "Create one to one (Slave:Master) RBE3 (Interpolation constraining Element)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBE3 > OneToOne"
---

## Description

Create one to one (Slave:Master) RBE3 (Interpolation constraining Element).

## Syntax

```psj
Connections.RigidElements.RBE3.OneToOne(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:17 -->
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

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bUpdateDispCS`

- The enable update displacement coordinate system.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:True -->
### `iEnableUpdateDispCS`

- The enable update displacement coordinate system.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:False -->
### `iEnableCornerOnly`

- The enable corner only.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {11-15}
Geometry.Part.Cube(
    ilAxialNodes=[4, 4, 4], strName="Cube _2", iPartColor=14903267)

Geometry.Part.Cube(
    dlOrigin=[0.012, 0.0, 0.0], 
    ilAxialNodes=[4, 4, 4], 
    strName="Cube _3", 
    iPartColor=7829501)

Connections.RigidElements.RBE3.OneToOne(
    crlMasterTargets=[Node(61, 87, 88, 64, 57, 71, 72, 60)], 
    crlSlaveTargets=[Node(6, 27, 28, 7, 2, 11, 12, 3)],
     listRbe3TermConnection=[(0, 63, 8), (1, 7, 8)],
     strName="RBE3 _3")
```
