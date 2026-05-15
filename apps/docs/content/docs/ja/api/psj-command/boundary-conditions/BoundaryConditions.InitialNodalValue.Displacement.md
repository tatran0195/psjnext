---
title: "BoundaryConditions.InitialNodalValue.Displacement()"
description: "Create Initial Dynamic"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InitialNodalValue > Displacement"
---

## Description

Create Initial Dynamic.

## Syntax

```psj
BoundaryConditions.InitialNodalValue.Displacement(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "InitialDisplacement1".

<!-- @since:5.0.1 @optional -->
### iType

- Specify the type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### vecInit

- Specify the initial.
- The default value is \[DFLT\_DBL,DFLT\_DBL,DFLT\_DBL].

<!-- @since:5.0.1 @optional -->
### bSelNode

- Specify the selection node.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### crNodeSet

- Specify the node set.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crTable

- Specify the table.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

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
BoundaryConditions.InitialNodalValue.Displacement(strName="InitialDisplacement1", iType=0, vecInit=[DFLT _DBL,DFLT _DBL,DFLT _DBL], bSelNode=False, crNodeSet=None, crTable=None, crCoord=None, crlTargets=[], crEdit=None)
```
