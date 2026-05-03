---
title: "BoundaryConditions.TemperatureLoads.ADVCFile()"
description: "Create temperature load by using ADVC file"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > TemperatureLoads > ADVCFile"
---

## Description

Create temperature load by using ADVC file.

## Syntax

```psj
BoundaryConditions.TemperatureLoads.ADVCFile(...)
```

## Inputs

### `strName` @type(String) @default("TemperatureLoadsADVC1")

- The name.

### `strFilePathName` @type(String) @default("")

- The file path name.

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
BoundaryConditions.TemperatureLoads.ADVCFile(strName="TemperatureLoadsADVC1", strFilePathName="", crTable=None, crlTargets=[], crEdit=None)
```
