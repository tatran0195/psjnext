---
title: "BoundaryConditions.TemperatureLoads.NastranPunch()"
description: "Create temperature load by using Nastran punch"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > TemperatureLoads > NastranPunch"
---

## Description

Create temperature load by using Nastran punch.

## Syntax

```psj
BoundaryConditions.TemperatureLoads.NastranPunch(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "TemperatureLoadsPunch1".

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

<!-- @since:5.1.0 @optional -->
### iLocalTemperatureUnit

- Specify the unit of temperature.
  - 0: K
  - 1: deg C
  - 2: deg F
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bUseAsMaterialReferenceTemp

- Specify the use as material reference temperature.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bSkipUnavailableNode

- Specify whether to skip nodes that do not exists in the model.
- The default value is _False_ .

<!-- @since:5.1.0 @optional -->
### vecUnavailableNodeId

- Specify the skip node ids.
- The default value is \[] .

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {7-9}
# Prepare mapping data as .pch
mapping _data _file = "C:/temp/test.pch"

# Prepare model
Geometry.Part.Cube(iPartColor=6409934)

BoundaryConditions.TemperatureLoads.NastranPunch(
    strName = "TemperatureLoadsPunch _1", 
    strFilePathName = mapping _data _file)
```
