---
id: Connections.RigidElements.RBar.OneToOne
title: Connections.RigidElements.RBar.OneToOne()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create RBar
---

## Description

Create RBar

## Syntax

```psj
Connections.RigidElements.RBar.OneToOne(strName="RBAR_1", crlMasterTargets=[], crlSlaveTargets=[], iMethod=17, iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None)
```

Ribbon: <menuselection>Connections &#187; RigidElements &#187; RBar &#187; OneToOne</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name.
- The default value is "RBAR_1".

### `crlMasterTargets`

- A _List of Cursor_ specifying the master target.
- The default value is [].

### `crlSlaveTargets`

- A _List of Cursor_ specifying the slave target.
- The default value is [].

### `iMethod`

- An _Integer_ specifying the method.
- The default value is 17.

### `iUlDOFs`

- An _Integer_ specifying the ul d o fs.
- The default value is 0.

### `dTol`

- A _Double_ specifying the tolerance.
- The default value is DFLT_DBL.

### `crCoord`

- A _Cursor_ specifying the coordinate.
- The default value is None.

### `crEdit`

- A _Cursor_ specifying the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.
