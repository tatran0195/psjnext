---
title: "Connections.SpringsDampers.Damper.AnyEntities11DoFS()"
description: "Create Damper Connection"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > SpringsDampers > Damper > AnyEntities11DoFS"
---

## Description

Create Damper Connection

## Syntax

```psj
Connections.SpringsDampers.Damper.AnyEntities11DoFS(iMethod, strName, crlMasterTargets, crlSlaveTargets, crCoordSys=None, iGround=0, dTolerance=0.0, vecTDamper=[0, 0, 0], vecRDamper=[0, 0, 0], crEdit=None, bUpdateDispCS=True)
```

## Inputs

### `iMethod` @type(Integer) @required

- The method.

### `strName` @type(String) @required

- The name.

### `crlMasterTargets` @type(List\[Cursor]) @required

- The master target.

### `crlSlaveTargets` @type(List\[Cursor]) @required

- The slave target.

### `crCoordSys` @type(Cursor) @default(None)

- The coordinate system.

### `iGround` @type(Integer) @default(0)

- The ground.

### `dTolerance` @type(Double) @default(0.0)

- The tolerance.

### `vecTDamper` @type(Vector) @default(\[0, 0, 0])

- The t damper.

### `vecRDamper` @type(Vector) @default(\[0, 0, 0])

- The r damper.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `bUpdateDispCS` @type(Boolean) @default(True)

- The update displacement coordinate system.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.SpringsDampers.Damper.AnyEntities11DoFS(iMethod, strName, crlMasterTargets, crlSlaveTargets, crCoordSys=None, iGround=0, dTolerance=0.0, vecTDamper=[0, 0, 0], vecRDamper=[0, 0, 0], crEdit=None, bUpdateDispCS=True)
```
