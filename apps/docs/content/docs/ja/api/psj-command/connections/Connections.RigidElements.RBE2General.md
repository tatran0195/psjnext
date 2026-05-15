---
title: "Connections.RigidElements.RBE2General()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBE2General"
macro _link: "[Rbe2](../../macro/connections/Rbe2)"
---

## Description

Unknown Description

## Syntax

```psj
Connections.RigidElements.RBE2General(iMethod, crlMasterTargets, crlSlaveTargets, iEType=2, strName="RBE2 _1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iDuplicateMode=-1)
```

## Inputs

<!-- @since:5.0.1 @required -->
### iMethod

- Specify the method.

<!-- @since:5.0.1 @required -->
### crlMasterTargets

- Specify the master target.

<!-- @since:5.0.1 @required -->
### crlSlaveTargets

- Specify the slave target.

<!-- @since:5.0.1 @optional -->
### iEType

- Specify the e type.
- The default value is 2.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "RBE2\_1".

<!-- @since:5.0.1 @optional -->
### crCoordSys

- Specify the coordinate system.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dTolerance

- Specify the tolerance.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iUlDOFs

- Specify the ul d o fs.
- The default value is 63.

<!-- @since:5.0.1 @optional -->
### dlVirtualNodePos

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
### iEnableUpdateDispCS

- Specify the enable update displacement coordinate system.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iEnableCornerOnly

- Specify the enable corner only.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDuplicateMode

- Specify the duplicate mode.
- The default value is -1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.RigidElements.RBE2General(iMethod, crlMasterTargets, crlSlaveTargets, iEType=2, strName="RBE2 _1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iDuplicateMode=-1)
```
