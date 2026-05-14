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

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @required -->
### `dFflux`

- The fflux.

<!-- @since:5.0.1 @type:Integer @required -->
### `iDistributionMethod`

- The distribution method.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crTable`

- The table.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.HeatFlux.SurfaceFlux(strName, dFflux, iDistributionMethod, crTable, crlTargets, crEdit=None)
```
