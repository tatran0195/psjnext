---
title: "BoundaryConditions.InitialTemperature.Constant()"
description: "Create initial temperature with constant value"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > InitialTemperature > Constant"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create initial temperature with constant value,

## Syntax

```psj
BoundaryConditions.InitialTemperature.Constant(...)
```

## Inputs

### `strName` @type(String) @default("InitialTemperature1")

- The initial temperature name.

### `dFTemp` @type(double) @default(0.0)

- The constant temperature.

### `iLocalTemperatureUnit` @type(Ingeter) @default(0) @since(5.1.0)

- The local temperature.

### `bUseDefault` @type(Boolean) @default(False)

- Enable/disable default temperature.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- List of target parts for initial temperature.

### `crEdit` @type(Cursor) @default(None)

- The initial temperature item which use for editing.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{2-7}
Geometry.Part.Cube()
BoundaryConditions.InitialTemperature.Constant(
        strName="InitialTemperature_1",
        iLocalTemperatureUnit=1, 
        dFTemp=278.15, 
        bUseDefault=True, 
        crlTargets=[Part(1)])
```
