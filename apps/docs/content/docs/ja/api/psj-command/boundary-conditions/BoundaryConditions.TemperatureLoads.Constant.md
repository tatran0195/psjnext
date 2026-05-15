---
title: "BoundaryConditions.TemperatureLoads.Constant()"
description: "Create temperature load constant"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > TemperatureLoads > Constant"
---

## Description

Create temperature load constant.

## Syntax

```psj
BoundaryConditions.TemperatureLoads.Constant(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @optional -->
### dTemperature

- Specify the temperature.
- The default value is 0.0.

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

<!-- @since:5.0.1 @optional -->
### bUseDefaultTemp

- Specify the use default temperature.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.TemperatureLoads.Constant(strName, dTemperature=0.0, crTable=None, crlTargets=[], crEdit=None, bUseDefaultTemp=False)
```
