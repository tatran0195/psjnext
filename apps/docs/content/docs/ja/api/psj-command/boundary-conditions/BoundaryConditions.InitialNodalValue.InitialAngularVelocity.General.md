---
title: "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General()"
description: "Create initial angular velocity for the general case"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InitialNodalValue > InitialAngularVelocity > General"
---

## Description

Create initial angular velocity for the general case.

## Syntax

```psj
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "InitialAngularVelocity1".

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
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General(strName="InitialAngularVelocity1", stData=LBC _DYNAMIC _INITIAL _CONDITION _DATA(), crlTargets=[], crEdit=None)
```
