---
title: "Connections.MassElements()"
description: "Connection new mass"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > MassElements"
---

## Description

Connection new mass

## Syntax

```psj
Connections.MassElements(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dMass`

- The mass.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iDof`

- The dof.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bDesigner`

- The for license switcher. If true, it is used in Designer.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The coordinate.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dOffset0`

- The offset0.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dOffset1`

- The offset1.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dOffset2`

- The offset2.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dInertia0`

- The inertia0.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dInertia1`

- The inertia1.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dInertia2`

- The inertia2.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dInertia3`

- The inertia3.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dInertia4`

- The inertia4.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dInertia5`

- The inertia5.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bUpdateDispCS`

- The update displacement coordinate system.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2-5}
Geometry.Part.Cube()
Connections.MassElements(strName="Mass1", crlTargets=[Node(5)], dMass=0.01, iDof=1, bDesigner=True, 
                        crCoordinate=None, dOffset0=0.0, dOffset1=0.0, dOffset2=0.0, dInertia0=0.0, 
                        dInertia1=0.0, dInertia2=0.0, dInertia3=0.0, dInertia4=0.0, dInertia5=0.0, 
                        crEdit=None, bUpdateDispCS=True)
```
