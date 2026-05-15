---
title: "BoundaryConditions.InitialElementalValue.InitialStress()"
description: "Create mapping stress"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InitialElementalValue > InitialStress"
---

## Description

Create mapping stress.

## Syntax

```psj
BoundaryConditions.InitialElementalValue.InitialStress(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "InitialStress1".

<!-- @since:5.0.1 @optional -->
### iDimension

- Specify the dimension.
- The default value is 2.

<!-- @since:5.0.1 @optional -->
### iElemCs

- Specify the element cs.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSXX

- Specify the s x x.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dSYY

- Specify the s y y.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dSXY

- Specify the s x y.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crTable

- Specify the table.
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
BoundaryConditions.InitialElementalValue.InitialStress(strName="InitialStress1", iDimension=2, iElemCs=0, dSXX=DFLT _DBL, dSYY=DFLT _DBL, dSXY=DFLT _DBL, crTable=None, crlTargets=[], crEdit=None)
```
