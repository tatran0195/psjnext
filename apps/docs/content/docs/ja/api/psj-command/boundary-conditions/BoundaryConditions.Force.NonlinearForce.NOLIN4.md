---
title: "BoundaryConditions.Force.NonlinearForce.NOLIN4()"
description: "Create nonlinear force NOLIN4"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Force > NonlinearForce > NOLIN4"
---

## Description

Create nonlinear force NOLIN4.

## Syntax

```psj
BoundaryConditions.Force.NonlinearForce.NOLIN4(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @optional -->
### dForceScale

- Specify the force scale.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dMomentScale

- Specify the moment scale.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dForcePowerA

- Specify the force power a.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dMomentPowerA

- Specify the moment power a.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iForcDir

- Specify the forc direction.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iForceDepends

- Specify the force depends.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMomentDir

- Specify the moment direction.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMomentDepends

- Specify the moment depends.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crCurCoord

- Specify the cur coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crlMasterTargets

- Specify the master target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlaveTargets

- Specify the slave target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Force.NonlinearForce.NOLIN4(strName, dForceScale=0.0, dMomentScale=0.0, dForcePowerA=0.0, dMomentPowerA=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCurCoord=None, crlMasterTargets=[], crlSlaveTargets=[], crEdit=None)
```
