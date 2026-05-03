---
title: "BoundaryConditions.TemperatureLoads.LbcInitialTemperature()"
description: "Boundary Conditions Lbc Initial Temperature"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > TemperatureLoads > LbcInitialTemperature"
---

## Description

Boundary Conditions Lbc Initial Temperature.

## Syntax

```psj
BoundaryConditions.TemperatureLoads.LbcInitialTemperature(...)
```

## Inputs

### `strName` @type(String) @default("InitialTemperature1")

- The name.

### `iType` @type(Integer) @default(0)

- The type.

### `dFTemp` @type(Double) @default(0.0)

- The temperature.

### `strFilePathName` @type(String) @default("")

- The file path name.

### `bUseDefault` @type(Boolean) @default(False)

- The use default.

### `crTable` @type(Cursor) @default(None)

- The table.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.TemperatureLoads.LbcInitialTemperature(strName="InitialTemperature1", iType=0, dFTemp=0.0, strFilePathName="", bUseDefault=False, crTable=None, crlTargets=[], crEdit=None)
```
