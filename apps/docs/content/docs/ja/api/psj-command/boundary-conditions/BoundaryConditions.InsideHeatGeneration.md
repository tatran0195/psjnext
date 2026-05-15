---
title: "BoundaryConditions.InsideHeatGeneration()"
description: "Create load boundary condition of inside heat generation"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InsideHeatGeneration"
---

## Description

Create load boundary condition of inside heat generation.

## Syntax

```psj
BoundaryConditions.InsideHeatGeneration(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "InsideHeatGeneration1".

<!-- @since:5.0.1 @optional -->
### dInsideFlux

- Specify the inside flux.
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
BoundaryConditions.InsideHeatGeneration(strName="InsideHeatGeneration1", dInsideFlux=DFLT _DBL, crTable=None, crlTargets=[], crEdit=None)
```
