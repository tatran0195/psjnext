---
title: "Test.Connection.RRod()"
description: "create RRod"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Test > Connection > RRod"
---

## Description

Create RRod

## Syntax

```psj
Test.Connection.RRod(rbarConnection=RBAR_CONNECTION(), iUlDOFs=1, dTol=0.0, crlMasterTargets=[], crlSlaveTargets=[])
```

## Inputs

### `rbarConnection` @type(RBAR\_CONNECTION) @default(RBAR\_CONNECTION())

- The connection.

### `iUlDOFs` @type(Integer) @default(1)

- The ul d o fs.

### `dTol` @type(Double) @default(0.0)

- The tolerance.

### `crlMasterTargets` @type(List\[Cursor]) @default(\[])

- The master target.

### `crlSlaveTargets` @type(List\[Cursor]) @default(\[])

- The slave target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.Connection.RRod(rbarConnection=RBAR_CONNECTION(), iUlDOFs=1, dTol=0.0, crlMasterTargets=[], crlSlaveTargets=[])
```
