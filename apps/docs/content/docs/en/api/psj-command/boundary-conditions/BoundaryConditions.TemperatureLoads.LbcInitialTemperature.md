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

<!-- @since:5.0.1 @type:String @optional @default:"InitialTemperature1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The type.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFTemp`

- The temperature.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strFilePathName`

- The file path name.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bUseDefault`

- The use default.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTable`

- The table.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.TemperatureLoads.LbcInitialTemperature(strName="InitialTemperature1", iType=0, dFTemp=0.0, strFilePathName="", bUseDefault=False, crTable=None, crlTargets=[], crEdit=None)
```
