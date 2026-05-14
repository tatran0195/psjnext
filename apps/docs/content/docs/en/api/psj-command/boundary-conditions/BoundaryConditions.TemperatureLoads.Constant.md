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

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTemperature`

- The temperature.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTable`

- The table.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bUseDefaultTemp`

- The use default temperature.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.TemperatureLoads.Constant(strName, dTemperature=0.0, crTable=None, crlTargets=[], crEdit=None, bUseDefaultTemp=False)
```
