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

<!-- @since:5.0.1 @type:String @optional @default:"TemperatureLoadsPunch1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strFilePathName`

- The file path name.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTable`

- The table.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iLocalTemperatureUnit`

- The unit of temperature.
  - 0: K
  - 1: deg C
  - 2: deg F

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bUseAsMaterialReferenceTemp`

- The use as material reference temperature.

<!-- @since:5.1.0 @type:Boolean @optional @default:False  -->
### `bSkipUnavailableNode`

- Whether to skip nodes that do not exists in the model.

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[]  -->
### `vecUnavailableNodeId`

- The skip node ids.

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
