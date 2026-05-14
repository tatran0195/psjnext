---
title: "Connections.RigidElements.RBE3.ToCenter()"
description: "Create one to many (Slave:Master) RBE3 (Interpolation constraining Element)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBE3 > ToCenter"
---

## Description

Create one to many (Slave:Master) RBE3 (Interpolation constraining Element).

## Syntax

```psj
Connections.RigidElements.RBE3.ToCenter(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:18 -->
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

- The type rbe3.

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

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bCornerOnly`

- The enable corner only.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:True -->
### `iEnableUpdateDispCS`

- The enable update displacement coordinate system.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:False -->
### `iEnableCornerOnly`

- The enable corner only.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {3-6}
Geometry.Part.Cylinder(bHollow=True, dTopInnerRadius=0.005, dBottomInnerRadius=0.005, iPartColor=15658599)

Connections.RigidElements.RBE3.ToCenter(crlMasterTargets=[Edge(1)], 
                                    listRbe3TermConnection=[(0, 63, 1), (1, 7, 1)], 
                                    strName="RBE3 _1", 
                                    dlVirtualNodePos=[0, 0.01, 0])
```
