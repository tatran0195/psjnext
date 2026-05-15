---
title: "BoundaryConditions.InitialTemperature.NastranPunch()"
description: "Load the temperature result output in Nastran Punch format and set as the initial temperature"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InitialTemperature > NastranPunch"
---

## Description

Load the temperature result output in Nastran Punch format and set as the initial temperature.

## Syntax

```psj
BoundaryConditions.InitialTemperature.NastranPunch(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the initial temperature name.
- The default value is "InitialTemperature1".

<!-- @since:5.0.1 @optional -->
### strFilePathName

- Specify the Nastran temperature result file path.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### iLocalTemperatureUnit

- Specify the local temperature.
- The default value is 0.

### `bUseDefault`

- A _Boolean_ enable/disable default temperature.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify list the target parts for initial temperature.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the initial temperature item which use for editing.
- The default value is None.

<!-- @since:5.1.0 @optional -->
### iTimeID

- Specify the time step in the result.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bSkipUnavailableNode

- Specify whether enable/disable skip unvailable nodes.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### vecUnvailableNodeIds

- Specify ids of unvailable nodes.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```pj {2-7}
# Prepare .pch file for setting
mapping _data _file = "C:/temp/test.pch"

Geometry.Part.Cube()
BoundaryConditions.InitialTemperature.NastranPunch(
        strName="InitialTemperature _1",
        iLocalTemperatureUnit=1, 
        strFilePathName = mapping _data _file,
        crlTargets=[Part(1)])
```
