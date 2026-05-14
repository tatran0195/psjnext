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

<!-- @since:5.0.1 @type:String @optional @default:"InitialTemperature1" -->
### `strName`

- The initial temperature name.

<!-- @since:5.0.1 @type:double @optional @default:0.0 -->
### `dFTemp`

- The constant temperature.

<!-- @since:5.1.0 @type:Ingeter @optional @default:0 -->
### `iLocalTemperatureUnit`

- The local temperature.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bUseDefault`

- The enable/disable default temperature.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The list of target parts for initial temperature.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The initial temperature item which use for editing.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2-7}
Geometry.Part.Cube()
BoundaryConditions.InitialTemperature.Constant(
        strName="InitialTemperature _1",
        iLocalTemperatureUnit=1, 
        dFTemp=278.15, 
        bUseDefault=True, 
        crlTargets=[Part(1)])
```
