---
title: "Connections.RigidElements.RBarGeneral()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBarGeneral"
---

## Description

Unknown Description

## Syntax

```psj
Connections.RigidElements.RBarGeneral(rbarConnection=RBAR _CONNECTION(), crlMasterTargets=[], crlSlaveTargets=[], iUlDOFs=0, dTol=DFLT _DBL, crCoord=None, crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @type:RBAR _CONNECTION @optional @default:RBAR _CONNECTION() -->
### `rbarConnection`

- The connection.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlMasterTargets`

- The master target.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSlaveTargets`

- The slave target.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iUlDOFs`

- The ul d o fs.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.RigidElements.RBarGeneral(rbarConnection=RBAR _CONNECTION(), crlMasterTargets=[], crlSlaveTargets=[], iUlDOFs=0, dTol=DFLT _DBL, crCoord=None, crEdit=None)
```
