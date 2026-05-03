---
title: "Connections.RigidElements.RBarGeneral()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > RigidElements > RBarGeneral"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Unknown Description

## Syntax

```psj
Connections.RigidElements.RBarGeneral(rbarConnection=RBAR_CONNECTION(), crlMasterTargets=[], crlSlaveTargets=[], iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None)
```

## Inputs

### `rbarConnection` @type(RBAR\_CONNECTION) @default(RBAR\_CONNECTION())

- The connection.

### `crlMasterTargets` @type(List\[Cursor]) @default(\[])

- The master target.

### `crlSlaveTargets` @type(List\[Cursor]) @default(\[])

- The slave target.

### `iUlDOFs` @type(Integer) @default(0)

- The ul d o fs.

### `dTol` @type(Double) @default(DFLT\_DBL)

- The tolerance.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.RigidElements.RBarGeneral(rbarConnection=RBAR_CONNECTION(), crlMasterTargets=[], crlSlaveTargets=[], iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None)
```
