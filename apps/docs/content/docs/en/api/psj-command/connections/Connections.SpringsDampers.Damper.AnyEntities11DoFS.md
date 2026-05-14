---
title: "Connections.SpringsDampers.Damper.AnyEntities11DoFS()"
description: "Create Damper Connection"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > SpringsDampers > Damper > AnyEntities11DoFS"
---

## Description

Create Damper Connection

## Syntax

```psj
Connections.SpringsDampers.Damper.AnyEntities11DoFS(iMethod, strName, crlMasterTargets, crlSlaveTargets, crCoordSys=None, iGround=0, dTolerance=0.0, vecTDamper=[0, 0, 0], vecRDamper=[0, 0, 0], crEdit=None, bUpdateDispCS=True)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @required -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlMasterTargets`

- The master target.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlSlaveTargets`

- The slave target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoordSys`

- The coordinate system.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iGround`

- The ground.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTolerance`

- The tolerance.

<!-- @since:5.0.1 @type:Vector @optional @default:[0, 0, 0] -->
### `vecTDamper`

- The t damper.

<!-- @since:5.0.1 @type:Vector @optional @default:[0, 0, 0] -->
### `vecRDamper`

- The r damper.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bUpdateDispCS`

- The update displacement coordinate system.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.SpringsDampers.Damper.AnyEntities11DoFS(iMethod, strName, crlMasterTargets, crlSlaveTargets, crCoordSys=None, iGround=0, dTolerance=0.0, vecTDamper=[0, 0, 0], vecRDamper=[0, 0, 0], crEdit=None, bUpdateDispCS=True)
```
