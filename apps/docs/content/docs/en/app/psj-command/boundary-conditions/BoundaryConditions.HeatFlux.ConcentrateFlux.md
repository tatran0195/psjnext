---
title: "BoundaryConditions.HeatFlux.ConcentrateFlux()"
description: "Create a heat flux condition"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > HeatFlux > ConcentrateFlux"
---

## Description

Create a heat flux condition.

## Syntax

```psj
BoundaryConditions.HeatFlux.ConcentrateFlux(...)
```

## Inputs

### `strName` @type(String) @default("ConcentrateHeatFlux1")

- The name.

### `dflux` @type(Double) @default(0.0)

- The heat flux value.

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
BoundaryConditions.HeatFlux.ConcentrateFlux(strName = "ConcentrateHeatFlux1", dflux=0.0, crTable=None, crlTargets=[], crEdit=None)
```
