---
title: "Connections.RigidElements.RBE2General()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > RigidElements > RBE2General"
macro_link: "[Rbe2](../../macro/connections/Rbe2)"
---

## Description

Unknown Description

## Syntax

```psj
Connections.RigidElements.RBE2General(iMethod, crlMasterTargets, crlSlaveTargets, iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iDuplicateMode=-1)
```

## Inputs

### `iMethod` @type(Integer) @required

- The method.

### `crlMasterTargets` @type(List\[Cursor]) @required

- The master target.

### `crlSlaveTargets` @type(List\[Cursor]) @required

- The slave target.

### `iEType` @type(Integer) @default(2)

- The e type.

### `strName` @type(String) @default("RBE2\_1")

- The name.

### `crCoordSys` @type(Cursor) @default(None)

- The coordinate system.

### `dTolerance` @type(Double) @default(0.0)

- The tolerance.

### `iUlDOFs` @type(Integer) @default(63)

- The ul d o fs.

### `dlVirtualNodePos` @type(Double List) @default(\[0, 0, 0])

- The virtual node position.

### `iSurfaceDef` @type(Integer) @default(0)

- The surface definition.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `iEnableUpdateDispCS` @type(Integer) @default(1)

- The enable update displacement coordinate system.

### `iEnableCornerOnly` @type(Integer) @default(0)

- The enable corner only.

### `iDuplicateMode` @type(Integer) @default(-1)

- The duplicate mode.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.RigidElements.RBE2General(iMethod, crlMasterTargets, crlSlaveTargets, iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iDuplicateMode=-1)
```
