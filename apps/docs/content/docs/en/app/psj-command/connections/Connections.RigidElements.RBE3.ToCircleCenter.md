---
title: "Connections.RigidElements.RBE3.ToCircleCenter()"
description: "Create RBE3"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > RigidElements > RBE3 > ToCircleCenter"
---

## Description

Create RBE3

## Syntax

```psj
Connections.RigidElements.RBE3.ToCircleCenter(iMethod=19, crlMasterTargets=[], crlSlaveTargets=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False)
```

## Inputs

### `iMethod` @type(Integer) @default(19)

- The method.

### `crlMasterTargets` @type(List\[Cursor]) @default(\[])

- The master target.

### `crlSlaveTargets` @type(List\[Cursor]) @default(\[])

- The slave target.

### `listRbe3TermConnection` @type(RBE3TERM\_CONNECTION List) @default(\[])

- The rbe3 term connection.

### `iTypeRBE3` @type(Integer) @default(3)

- The type r e3.

### `strName` @type(String) @default("")

- The name.

### `crCoordSys` @type(Cursor) @default(None)

- The coordinate system.

### `dTolerance` @type(Double) @default(0.0)

- The tolerance.

### `dlVirtualNodePos` @type(Double List) @default(\[0, 0, 0])

- The virtual node position.

### `iSurfaceDef` @type(Integer) @default(0)

- The surface definition.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `iEnableUpdateDispCS` @type(Integer) @default(True)

- The enable update displacement coordinate system.

### `iEnableCornerOnly` @type(Integer) @default(False)

- The enable corner only.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.RigidElements.RBE3.ToCircleCenter(iMethod=19, crlMasterTargets=[], crlSlaveTargets=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False)
```
