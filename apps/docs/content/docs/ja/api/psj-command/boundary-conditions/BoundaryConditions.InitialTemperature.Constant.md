---
title: "BoundaryConditions.InitialTemperature.Constant()"
description: "Create initial temperature with constant value"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InitialTemperature > Constant"
---

## Description

Create initial temperature with constant value,

## Syntax

```psj
BoundaryConditions.InitialTemperature.Constant(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the initial temperature name.
- The default value is "InitialTemperature1".

<!-- @since:5.0.1 @optional -->
### dFTemp

- Specify the constant temperature.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iLocalTemperatureUnit

- Specify the local temperature.
- The default value is 0.

### `bUseDefault`

- A _Boolean_ enable/disable default temperature.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify list of target parts for initial temperature.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the initial temperature item which use for editing.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```pj {2-7}
Geometry.Part.Cube()
BoundaryConditions.InitialTemperature.Constant(
        strName="InitialTemperature _1",
        iLocalTemperatureUnit=1, 
        dFTemp=278.15, 
        bUseDefault=True, 
        crlTargets=[Part(1)])
```
