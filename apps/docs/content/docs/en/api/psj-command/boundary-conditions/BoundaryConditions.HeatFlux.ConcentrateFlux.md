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

<!-- @since:5.0.1 @type:String @optional @default:"ConcentrateHeatFlux1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dflux`

- The heat flux value.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTable`

- The table.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.HeatFlux.ConcentrateFlux(strName = "ConcentrateHeatFlux1", dflux=0.0, crTable=None, crlTargets=[], crEdit=None)
```
