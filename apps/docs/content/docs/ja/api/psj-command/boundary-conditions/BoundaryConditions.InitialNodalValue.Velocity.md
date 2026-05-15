---
title: "BoundaryConditions.InitialNodalValue.Velocity()"
description: "Create initial velocity"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InitialNodalValue > Velocity"
---

## Description

Create initial velocity.

## Syntax

```psj
BoundaryConditions.InitialNodalValue.Velocity(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "InitialRotationAngle1".

<!-- @since:5.0.1 @optional -->
### stData

- Specify the data.
- The default value is LBC\_DYNAMIC\_INITIAL\_CONDITION\_DATA().

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
BoundaryConditions.InitialNodalValue.Velocity(strName="InitialRotationAngle1", stData=LBC _DYNAMIC _INITIAL _CONDITION _DATA(), crlTargets=[], crEdit=None)
```
