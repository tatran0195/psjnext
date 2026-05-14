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

<!-- @since:5.0.1 @type:String @optional @default:"TemperatureLoadsADVC1" -->
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

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.TemperatureLoads.ADVCFile(strName="TemperatureLoadsADVC1", strFilePathName="", crTable=None, crlTargets=[], crEdit=None)
```
