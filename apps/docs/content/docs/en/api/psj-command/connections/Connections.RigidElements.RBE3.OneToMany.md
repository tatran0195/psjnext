---
title: "Connections.RigidElements.RBE3.OneToMany()"
description: "Create one to many (Slave:Master) RBE3 (Interpolation constraining Element)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBE3 > OneToMany"
---

## Description

Create one to many (Slave:Master) RBE3 (Interpolation constraining Element).

## Syntax

```psj
Connections.RigidElements.RBE3.OneToMany(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:16 -->
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

A Cursor specifying the created RBE3 connection.

## Sample Code

```psj {6-9}
# Prepare model
Geometry.Part.Cube(iPartColor=7697908)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _2", iPartColor=14903267)

# Create the connection
Connections.RigidElements.RBE3.OneToMany(crlMasterTargets=[Node(589, 496, 493)], 
                                        crlSlaveTargets=[Node(84)], 
                                        listRbe3TermConnection=[(0, 63, 1), (1, 7, 3)], 
                                        strName="RBE3 _1")
```
