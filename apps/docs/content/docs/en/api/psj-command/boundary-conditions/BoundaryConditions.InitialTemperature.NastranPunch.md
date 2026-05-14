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

<!-- @since:5.0.1 @type:String @optional @default:"InitialTemperature1" -->
### `strName`

- The initial temperature name.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strFilePathName`

- The Nastran temperature result file path.

<!-- @since:5.1.0 @type:Ingeter @optional @default:0 -->
### `iLocalTemperatureUnit`

- The local temperature.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bUseDefault`

- The enable/disable default temperature.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The list the target parts for initial temperature.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The initial temperature item which use for editing.

<!-- @since:5.1.0 @type:Ingeter @optional @default:0 -->
### `iTimeID`

- The time step in the result.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bSkipUnavailableNode`

- Whether enable/disable skip unvailable nodes.

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[] -->
### `vecUnvailableNodeIds`

- The ids of unvailable nodes.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2-7}
# Prepare .pch file for setting
mapping _data _file = "C:/temp/test.pch"

Geometry.Part.Cube()
BoundaryConditions.InitialTemperature.NastranPunch(
        strName="InitialTemperature _1",
        iLocalTemperatureUnit=1, 
        strFilePathName = mapping _data _file,
        crlTargets=[Part(1)])
```
