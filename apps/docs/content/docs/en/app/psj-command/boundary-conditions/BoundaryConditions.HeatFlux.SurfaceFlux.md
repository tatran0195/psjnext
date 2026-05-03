---
title: "BoundaryConditions.HeatFlux.SurfaceFlux()"
description: "Create a surface flux"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > HeatFlux > SurfaceFlux"
---

## Description

Create a surface flux.

## Syntax

```psj
BoundaryConditions.HeatFlux.SurfaceFlux(...)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `dFflux` @type(Double) @required

- The fflux.

### `iDistributionMethod` @type(Integer) @required

- The distribution method.

### `crTable` @type(Cursor) @required

- The table.

### `crlTargets` @type(List\[Cursor]) @required

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.HeatFlux.SurfaceFlux(strName, dFflux, iDistributionMethod, crTable, crlTargets, crEdit=None)
```
