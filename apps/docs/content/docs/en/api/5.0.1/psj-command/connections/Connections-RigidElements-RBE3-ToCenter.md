---
id: Connections.RigidElements.RBE3.ToCenter
title: Connections.RigidElements.RBE3.ToCenter()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create RBE3
---

## Description

Create RBE3

## Syntax

```psj
Connections.RigidElements.RBE3.ToCenter(iMethod=18, crlMasterTargets=[], crlSlaveTargets=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False)
```

Ribbon: <menuselection>Connections &#187; RigidElements &#187; RBE3 &#187; ToCenter</menuselection>

## Inputs

### `iMethod`

- An _Integer_ specifying the method.
- The default value is 18.

### `crlMasterTargets`

- A _List of Cursor_ specifying the master target.
- The default value is [].

### `crlSlaveTargets`

- A _List of Cursor_ specifying the slave target.
- The default value is [].

### `listRbe3TermConnection`

- A _RBE3TERM_CONNECTION List_ specifying the rbe3 term connection.
- The default value is [].

### `iTypeRBE3`

- An _Integer_ specifying the type r e3.
- The default value is 3.

### `strName`

- A _String_ specifying the name.
- The default value is "".

### `crCoordSys`

- A _Cursor_ specifying the coordinate system.
- The default value is None.

### `dTolerance`

- A _Double_ specifying the tolerance.
- The default value is 0.0.

### `dlVirtualNodePos`

- A _Double List_ specifying the virtual node position.
- The default value is [0, 0, 0].

### `iSurfaceDef`

- An _Integer_ specifying the surface definition.
- The default value is 0.

### `crEdit`

- A _Cursor_ specifying the edit.
- The default value is None.

### `iEnableUpdateDispCS`

- An _Integer_ specifying the enable update displacement coordinate system.
- The default value is True.

### `iEnableCornerOnly`

- An _Integer_ specifying the enable corner only.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.
