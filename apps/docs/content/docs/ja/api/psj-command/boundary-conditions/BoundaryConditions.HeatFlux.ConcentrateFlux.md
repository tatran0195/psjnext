---
title: "BoundaryConditions.HeatFlux.ConcentrateFlux()"
description: "Create a heat flux condition"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > HeatFlux > ConcentrateFlux"
---

## Description

Create a heat flux condition.

## Syntax

```psj
BoundaryConditions.HeatFlux.ConcentrateFlux(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "ConcentrateHeatFlux1".

<!-- @since:5.0.1 @optional -->
### dflux

- Specify the heat flux value.
- The default value is _0.0_.

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
BoundaryConditions.HeatFlux.ConcentrateFlux(strName = "ConcentrateHeatFlux1", dflux=0.0, crTable=None, crlTargets=[], crEdit=None)
```
