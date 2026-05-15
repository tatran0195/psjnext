---
title: "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus()"
description: "Create initial angular velocity for the Abaqus solver"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InitialNodalValue > InitialAngularVelocity > Abaqus"
---

## Description

Create initial angular velocity for the Abaqus solver.

## Syntax

```psj
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "InitialAngularVelocityAbaqus1".

<!-- @since:5.0.1 @optional -->
### dVelocity

- Specify the velocity.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### strFirstCoord

- Specify the first coordinate.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### strSecondCoord

- Specify the second coordinate.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus(strName="InitialAngularVelocityAbaqus1", dVelocity=DFLT _DBL, strFirstCoord="", strSecondCoord="", crlTargets=[], crEdit=None)
```
