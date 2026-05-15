---
title: "BoundaryConditions.HeatFlux.SurfaceFlux()"
description: "Create a surface flux"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > HeatFlux > SurfaceFlux"
---

## Description

Create a surface flux.

## Syntax

```psj
BoundaryConditions.HeatFlux.SurfaceFlux(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### dFflux

- Specify the fflux.

<!-- @since:5.0.1 @required -->
### iDistributionMethod

- Specify the distribution method.

<!-- @since:5.0.1 @required -->
### crTable

- Specify the table.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the target.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.HeatFlux.SurfaceFlux(strName, dFflux, iDistributionMethod, crTable, crlTargets, crEdit=None)
```
