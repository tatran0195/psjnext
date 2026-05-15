---
title: "BoundaryConditions.TemperatureLoads.LbcInitialTemperature()"
description: "Boundary Conditions Lbc Initial Temperature"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > TemperatureLoads > LbcInitialTemperature"
---

## Description

Boundary Conditions Lbc Initial Temperature.

## Syntax

```psj
BoundaryConditions.TemperatureLoads.LbcInitialTemperature(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "InitialTemperature1".

<!-- @since:5.0.1 @optional -->
### iType

- Specify the type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dFTemp

- Specify the temperature.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### strFilePathName

- Specify the file path name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### bUseDefault

- Specify the use default.
- The default value is False.

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
BoundaryConditions.TemperatureLoads.LbcInitialTemperature(strName="InitialTemperature1", iType=0, dFTemp=0.0, strFilePathName="", bUseDefault=False, crTable=None, crlTargets=[], crEdit=None)
```
