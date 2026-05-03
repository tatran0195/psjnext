---
title: "BoundaryConditions.Pressure.Hydrostatic()"
description: "Create hydrostatic pressure"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Pressure > Hydrostatic"
---

## Description

Create hydrostatic pressure.

## Syntax

```psj
BoundaryConditions.Pressure.Hydrostatic(...)
```

## Inputs

### `strName` @type(String) @default("PressureHydrostatic1")

- The name.

### `dFHPressure` @type(Double) @default(0.0)

- The h pressure.

### `dFDensity` @type(Double) @default(0.0)

- The density.

### `iDensityUnit` @type(Integer) @default(0)

- The density unit.

### `dFGravity` @type(Double) @default(0.0)

- The gravity.

### `iGravityUnit` @type(Integer) @default(0)

- The gravity unit.

### `iGravityDir` @type(Integer) @default(0)

- The gravity direction.

### `dFWaterSuface` @type(Double) @default(0.0)

- The water suface.

### `iSufaceUnit` @type(Integer) @default(0)

- The suface unit.

### `iDistributionMethod` @type(Integer) @default(0)

- The distribution method.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Pressure.Hydrostatic(strName="PressureHydrostatic1", dFHPressure=0.0, dFDensity=0.0, iDensityUnit=0, dFGravity=0.0, iGravityUnit=0, iGravityDir=0, dFWaterSuface=0.0, iSufaceUnit=0, iDistributionMethod=0, crlTargets=[], crEdit=None)
```
