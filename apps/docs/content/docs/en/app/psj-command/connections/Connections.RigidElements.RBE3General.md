---
title: "Connections.RigidElements.RBE3General()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > RigidElements > RBE3General"
macro_link: "[Rbe3](../../macro/connections/Rbe3)"
---

## Description

Unknown Description

## Syntax

```psj
Connections.RigidElements.RBE3General(iMethod=0, crlMasterTargets=[], crlSlaveTargets=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, posVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, bUpdateDispCS=True, bCornerOnly=False)
```

## Inputs

### `iMethod` @type(Integer) @default(0)

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

### `posVirtualNodePos` @type(Position) @default(\[0, 0, 0])

- The virtual node position.

### `iSurfaceDef` @type(Integer) @default(0)

- The surface definition.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `bUpdateDispCS` @type(Boolean) @default(True)

- The update displacement coordinate system.

### `bCornerOnly` @type(Boolean) @default(False)

- The corner only.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.RigidElements.RBE3General(iMethod=0, crlMasterTargets=[], crlSlaveTargets=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, posVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, bUpdateDispCS=True, bCornerOnly=False)
```
