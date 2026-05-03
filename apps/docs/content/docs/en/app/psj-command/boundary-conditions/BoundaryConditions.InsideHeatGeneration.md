---
title: "BoundaryConditions.InsideHeatGeneration()"
description: "Create load boundary condition of inside heat generation"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > InsideHeatGeneration"
---

## Description

Create load boundary condition of inside heat generation.

## Syntax

```psj
BoundaryConditions.InsideHeatGeneration(...)
```

## Inputs

### `strName` @type(String) @default("InsideHeatGeneration1")

- The name.

### `dInsideFlux` @type(Double) @default(DFLT\_DBL)

- The inside flux.

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
BoundaryConditions.InsideHeatGeneration(strName="InsideHeatGeneration1", dInsideFlux=DFLT_DBL, crTable=None, crlTargets=[], crEdit=None)
```
