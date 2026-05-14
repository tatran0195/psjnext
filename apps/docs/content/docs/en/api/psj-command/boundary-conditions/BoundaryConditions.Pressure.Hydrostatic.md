---
title: "BoundaryConditions.Pressure.Hydrostatic()"
description: "Create hydrostatic pressure"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Pressure > Hydrostatic"
---

## Description

Create hydrostatic pressure.

## Syntax

```psj
BoundaryConditions.Pressure.Hydrostatic(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"PressureHydrostatic1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFHPressure`

- The h pressure.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFDensity`

- The density.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDensityUnit`

- The density unit.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFGravity`

- The gravity.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iGravityUnit`

- The gravity unit.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iGravityDir`

- The gravity direction.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFWaterSuface`

- The water suface.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSufaceUnit`

- The suface unit.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDistributionMethod`

- The distribution method.

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
BoundaryConditions.Pressure.Hydrostatic(strName="PressureHydrostatic1", dFHPressure=0.0, dFDensity=0.0, iDensityUnit=0, dFGravity=0.0, iGravityUnit=0, iGravityDir=0, dFWaterSuface=0.0, iSufaceUnit=0, iDistributionMethod=0, crlTargets=[], crEdit=None)
```
