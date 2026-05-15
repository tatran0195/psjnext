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

<!-- @since:5.0.1 @required -->
### iMethod

- Specify the method.

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### crlMasterTargets

- Specify the master target.

<!-- @since:5.0.1 @required -->
### crlSlaveTargets

- Specify the slave target.

<!-- @since:5.0.1 @optional -->
### crCoordSys

- Specify the coordinate system.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iGround

- Specify the ground.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTolerance

- Specify the tolerance.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### vecTDamper

- Specify the t damper.
- The default value is \[0, 0, 0].

<!-- @since:5.0.1 @optional -->
### vecRDamper

- Specify the r damper.
- The default value is \[0, 0, 0].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### bUpdateDispCS

- Specify the update displacement coordinate system.
- The default value is True.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.SpringsDampers.Damper.AnyEntities11DoFS(iMethod, strName, crlMasterTargets, crlSlaveTargets, crCoordSys=None, iGround=0, dTolerance=0.0, vecTDamper=[0, 0, 0], vecRDamper=[0, 0, 0], crEdit=None, bUpdateDispCS=True)
```
