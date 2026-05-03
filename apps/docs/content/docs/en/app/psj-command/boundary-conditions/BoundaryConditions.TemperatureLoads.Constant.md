---
title: "BoundaryConditions.TemperatureLoads.Constant()"
description: "Create temperature load constant"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > TemperatureLoads > Constant"
---

## Description

Create temperature load constant.

## Syntax

```psj
BoundaryConditions.TemperatureLoads.Constant(...)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `dTemperature` @type(Double) @default(0.0)

- The temperature.

### `crTable` @type(Cursor) @default(None)

- The table.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `bUseDefaultTemp` @type(Boolean) @default(False)

- The use default temperature.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.TemperatureLoads.Constant(strName, dTemperature=0.0, crTable=None, crlTargets=[], crEdit=None, bUseDefaultTemp=False)
```
