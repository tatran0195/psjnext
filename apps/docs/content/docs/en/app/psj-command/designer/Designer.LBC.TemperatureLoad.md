---
title: "Designer.LBC.TemperatureLoad()"
description: "create temperature load Desiner"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Designer > LBC > TemperatureLoad"
---

## Description

Create temperature load Desiner

## Syntax

```psj
Designer.LBC.TemperatureLoad(strName="", iDnType=0, dFTemp=0, strDstrFilePathName="", crDcrTable=None, crlTargets=[], crEdit=None, bDbUseAsMaterialReferenceTemp=False)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `iDnType` @type(Integer) @default(0)

- The dn type.

### `dFTemp` @type(Double) @default(0)

- The temperature.

### `strDstrFilePathName` @type(String) @default("")

- The dstr file path name.

### `crDcrTable` @type(Cursor) @default(None)

- The dcr table.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `bDbUseAsMaterialReferenceTemp` @type(Boolean) @default(False)

- The db use as material reference temperature.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Designer.LBC.TemperatureLoad(strName="", iDnType=0, dFTemp=0, strDstrFilePathName="", crDcrTable=None, crlTargets=[], crEdit=None, bDbUseAsMaterialReferenceTemp=False)
```
