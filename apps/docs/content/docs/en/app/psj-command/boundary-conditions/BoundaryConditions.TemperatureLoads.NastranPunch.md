---
title: "BoundaryConditions.TemperatureLoads.NastranPunch()"
description: "Create temperature load by using Nastran punch"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > TemperatureLoads > NastranPunch"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create temperature load by using Nastran punch.

## Syntax

```psj
BoundaryConditions.TemperatureLoads.NastranPunch(...)
```

## Inputs

### `strName` @type(String) @default("TemperatureLoadsPunch1")

- The name.

### `strFilePathName` @type(String) @default("")

- The file path name.

### `crTable` @type(Cursor) @default(None)

- The table.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `iLocalTemperatureUnit` @type(Integer) @default(0) @since(5.1.0)

- The unit of temperature.
  - 0: K
  - 1: deg C
  - 2: deg F

### `bUseAsMaterialReferenceTemp` @type(Boolean) @default(False)

- The use as material reference temperature.

### `bSkipUnavailableNode` @type(Boolean) @default(False ) @since(5.1.0)

- Whether to skip nodes that do not exists in the model.

### `vecUnavailableNodeId` @type(List\[Integer]) @default(\[] ) @since(5.1.0)

- The skip node ids.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{7-9}
# Prepare mapping data as .pch
mapping_data_file = "C:/temp/test.pch"

# Prepare model
Geometry.Part.Cube(iPartColor=6409934)

BoundaryConditions.TemperatureLoads.NastranPunch(
    strName = "TemperatureLoadsPunch_1", 
    strFilePathName = mapping_data_file)
```
