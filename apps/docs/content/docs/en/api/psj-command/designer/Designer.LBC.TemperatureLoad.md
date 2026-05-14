---
title: "Designer.LBC.TemperatureLoad()"
description: "create temperature load Desiner"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Designer > LBC > TemperatureLoad"
---

## Description

Create temperature load Desiner

## Syntax

```psj
Designer.LBC.TemperatureLoad(strName="", iDnType=0, dFTemp=0, strDstrFilePathName="", crDcrTable=None, crlTargets=[], crEdit=None, bDbUseAsMaterialReferenceTemp=False)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDnType`

- The dn type.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dFTemp`

- The temperature.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strDstrFilePathName`

- The dstr file path name.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crDcrTable`

- The dcr table.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDbUseAsMaterialReferenceTemp`

- The db use as material reference temperature.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Designer.LBC.TemperatureLoad(strName="", iDnType=0, dFTemp=0, strDstrFilePathName="", crDcrTable=None, crlTargets=[], crEdit=None, bDbUseAsMaterialReferenceTemp=False)
```
