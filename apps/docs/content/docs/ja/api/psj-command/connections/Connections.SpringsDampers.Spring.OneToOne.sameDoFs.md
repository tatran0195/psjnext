---
title: "Connections.SpringsDampers.Spring.OneToOne.sameDoFs()"
description: "Spring connection One to One same DOFs"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > SpringsDampers > Spring > OneToOne > sameDoFs"
---

## Description

Spring connection One to One same DOFs

## Syntax

```psj
Connections.SpringsDampers.Spring.OneToOne.sameDoFs(iMethod=0, strName="SPRING", crlMasterTargets=[], crlSlaveTargets=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT _DBL, dStressCoef=DFLT _DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "SPRING".

<!-- @since:5.0.1 @optional -->
### crlMasterTargets

- Specify the master target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlaveTargets

- Specify the slave target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crCoordSys

- Specify the coordinate system.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iSpringType

- Specify the spring type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iGround

- Specify the ground.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTolerance

- Specify the tolerance.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iDirection

- Specify the direction.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDistributeMode

- Specify the distribute mode.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDof1

- Specify the DOF 1.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDof2

- Specify the DOF 2.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDampCoef

- Specify the damp coefficient .
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dStressCoef

- Specify the stress coefficient .
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### posTStiffness

- Specify the t stiffness.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### posRStiffness

- Specify the r stiffness.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### bUpdateDispCS

- Specify the update displacement coordinate system.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.SpringsDampers.Spring.OneToOne.sameDoFs(iMethod=0, strName="SPRING", crlMasterTargets=[], crlSlaveTargets=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT _DBL, dStressCoef=DFLT _DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None)
```
