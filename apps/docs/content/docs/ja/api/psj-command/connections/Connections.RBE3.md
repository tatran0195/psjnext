---
title: "Connections.RBE3()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RBE3"
macro _link: "[Rbe3](../../macro/connections/Rbe3)"
---

## Description

Unknown Description

## Syntax

```psj
Connections.RBE3(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crlMasterTargets

- Specify the master target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlaveTargets

- Specify the slave target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listRbe3TermConnection

- Specify the rbe3 term connection.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iTypeRBE3

- Specify the type r e3.
- The default value is 3.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crCoordSys

- Specify the coordinate system.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dTolerance

- Specify the tolerance.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### posVirtualNodePos

- Specify the virtual node position.
- The default value is \[0, 0, 0].

<!-- @since:5.0.1 @optional -->
### iSurfaceDef

- Specify the surface definition.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### bUpdateDispCS

- Specify the update displacement coordinate system.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### bCornerOnly

- Specify the corner only.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.RBE3(iMethod=0, crlMasterTargets=[], crlSlaveTargets=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, posVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, bUpdateDispCS=True, bCornerOnly=False)
```
