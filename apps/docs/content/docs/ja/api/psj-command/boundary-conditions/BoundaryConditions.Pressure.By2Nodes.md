---
title: "BoundaryConditions.Pressure.By2Nodes()"
description: "Create load boundary condition of 2nodes pressure"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Pressure > By2Nodes"
---

## Description

Create load boundary condition of 2nodes pressure.

## Syntax

```psj
BoundaryConditions.Pressure.By2Nodes(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "PressureLinear1".

<!-- @since:5.0.1 @optional -->
### crNodeA

- Specify the node a.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dPressureA

- Specify the pressure a.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iNodeAUnit

- Specify the node a unit.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crNodeB

- Specify the node .
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dPressureB

- Specify the pressure .
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iNodeBUnit

- Specify the node unit.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDirection

- Specify the direction.
- The default value is 0.

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
BoundaryConditions.Pressure.By2Nodes(strName="PressureLinear1", crNodeA=None, dPressureA=0.0, iNodeAUnit=0, crNodeB=None, dPressureB=0.0, iNodeBUnit=0, iDirection=0, crlTargets=[], crEdit=None)
```
