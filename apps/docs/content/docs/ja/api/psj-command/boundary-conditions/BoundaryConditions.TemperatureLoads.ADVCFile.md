---
title: "BoundaryConditions.TemperatureLoads.ADVCFile()"
description: "Create temperature load by using ADVC file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > TemperatureLoads > ADVCFile"
---

## Description

Create temperature load by using ADVC file.

## Syntax

```psj
BoundaryConditions.TemperatureLoads.ADVCFile(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "TemperatureLoadsADVC1".

<!-- @since:5.0.1 @optional -->
### strFilePathName

- Specify the file path name.
- The default value is "".

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
BoundaryConditions.TemperatureLoads.ADVCFile(strName="TemperatureLoadsADVC1", strFilePathName="", crTable=None, crlTargets=[], crEdit=None)
```
