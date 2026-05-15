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

<!-- @since:5.0.1 @optional -->
### rbarConnection

- Specify the connection.
- The default value is RBAR\_CONNECTION().

<!-- @since:5.0.1 @optional -->
### crlMasterTargets

- Specify the master target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlaveTargets

- Specify the slave target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iUlDOFs

- Specify the ul d o fs.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is _None_.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.RigidElements.RBarGeneral(rbarConnection=RBAR _CONNECTION(), crlMasterTargets=[], crlSlaveTargets=[], iUlDOFs=0, dTol=DFLT _DBL, crCoord=None, crEdit=None)
```
