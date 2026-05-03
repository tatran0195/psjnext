---
title: "BoundaryConditions.InitialTemperature.NastranPunch()"
description: "Load the temperature result output in Nastran Punch format and set as the initial temperature"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > InitialTemperature > NastranPunch"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Load the temperature result output in Nastran Punch format and set as the initial temperature.

## Syntax

```psj
BoundaryConditions.InitialTemperature.NastranPunch(...)
```

## Inputs

### `strName` @type(String) @default("InitialTemperature1")

- The initial temperature name.

### `strFilePathName` @type(String) @default("")

- The Nastran temperature result file path.

### `iLocalTemperatureUnit` @type(Ingeter) @default(0) @since(5.1.0)

- The local temperature.

### `bUseDefault` @type(Boolean) @default(False)

- Enable/disable default temperature.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- List the target parts for initial temperature.

### `crEdit` @type(Cursor) @default(None)

- The initial temperature item which use for editing.

### `iTimeID` @type(Ingeter) @default(0) @since(5.1.0)

- The time step in the result.

### `bSkipUnavailableNode` @type(Boolean) @default(False) @since(5.1.0)

- Whether enable/disable skip unvailable nodes.

### `vecUnvailableNodeIds` @type(List\[Integer]) @default(\[]) @since(5.1.0)

- Ids of unvailable nodes.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{2-7}
# Prepare .pch file for setting
mapping_data_file = "C:/temp/test.pch"

Geometry.Part.Cube()
BoundaryConditions.InitialTemperature.NastranPunch(
        strName="InitialTemperature_1",
        iLocalTemperatureUnit=1, 
        strFilePathName = mapping_data_file,
        crlTargets=[Part(1)])
```
