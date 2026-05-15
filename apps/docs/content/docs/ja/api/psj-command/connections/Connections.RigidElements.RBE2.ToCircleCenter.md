---
title: "Connections.RigidElements.RBE2.ToCircleCenter()"
description: "create RBE2"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBE2 > ToCircleCenter"
---

## Description

Create RBE2

## Syntax

```psj
Connections.RigidElements.RBE2.ToCircleCenter(iMethod=19, crlMasterTargets=[], crlSlaveTargets=[], iEType=2, strName="RBE2 _1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 19.

<!-- @since:5.0.1 @optional -->
### crlMasterTargets

- Specify the master target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlaveTargets

- Specify the slave target.
- The default value is \[].

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

<!-- @since:5.1.0 @optional -->
### iEnableCheckDuplicate

- Specify the enable check dulplicate.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iDuplicateMode

- Specify the duplicate mode.
- The default value is 0.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iEnableCheckDulplicate

- Specify the enable check dulplicate.
- The default value is 1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.RigidElements.RBE2.ToCircleCenter(iMethod=19, crlMasterTargets=[], crlSlaveTargets=[], iEType=2, strName="RBE2 _1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0)
```
