---
title: "BoundaryConditions.Force.NonlinearForce.NOLIN1()"
description: "Create Nonlinear Force of NOLIN1(Table)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Force > NonlinearForce > NOLIN1"
---

## Description

Create Nonlinear Force of NOLIN1(Table).

## Syntax

```psj
BoundaryConditions.Force.NonlinearForce.NOLIN1(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "NonlinearForce1\_1".

<!-- @since:5.0.1 @optional -->
### dForceScale

- Specify the force scale.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dMomentScale

- Specify the moment scale.
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
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crForceTable

- Specify the force table.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crMomentTable

- Specify the moment table.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crlMaster

- Specify the master.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlave

- Specify the slave.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Force.NonlinearForce.NOLIN1(strName="NonlinearForce1 _1", dForceScale=0.0, dMomentScale=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCoord=None, crForceTable=None, crMomentTable=None, crlMaster=[], crlSlave=[], crEdit=None)
```
