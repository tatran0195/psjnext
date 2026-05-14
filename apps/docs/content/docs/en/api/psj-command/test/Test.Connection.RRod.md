---
title: "Test.Connection.RRod()"
description: "create RRod"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Test > Connection > RRod"
---

## Description

Create RRod

## Syntax

```psj
Test.Connection.RRod(rbarConnection=RBAR _CONNECTION(), iUlDOFs=1, dTol=0.0, crlMasterTargets=[], crlSlaveTargets=[])
```

## Inputs

<!-- @since:5.0.1 @type:RBAR _CONNECTION @optional @default:RBAR _CONNECTION() -->
### `rbarConnection`

- The connection.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iUlDOFs`

- The ul d o fs.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlMasterTargets`

- The master target.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSlaveTargets`

- The slave target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.Connection.RRod(rbarConnection=RBAR _CONNECTION(), iUlDOFs=1, dTol=0.0, crlMasterTargets=[], crlSlaveTargets=[])
```
