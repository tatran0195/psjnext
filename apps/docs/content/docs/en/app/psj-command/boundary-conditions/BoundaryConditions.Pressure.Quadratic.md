---
title: "BoundaryConditions.Pressure.Quadratic()"
description: "Create quadratic pressure"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Pressure > Quadratic"
---

## Description

Create quadratic pressure.

## Syntax

```psj
BoundaryConditions.Pressure.Quadratic(...)
```

## Inputs

### `strName` @type(String) @default("PressureQuadratic1")

- The name.

### `dA` @type(Double) @default(0.0)

- The a.

### `dB` @type(Double) @default(0.0)

- The .

### `crCoordinate` @type(Cursor) @default(None)

- The coordinate.

### `dAngleRange` @type(Double) @default(0.0)

- The angle range.

### `iPressureDirectionMode` @type(Integer) @default(0)

- The pressure direction mode.

### `dlPressureDirection` @type(Double List) @default(\[0.0,0.0,0.0])

- The pressure direction.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Pressure.Quadratic(strName="PressureQuadratic1", dA=0.0, dB=0.0, crCoordinate=None, dAngleRange=0.0, iPressureDirectionMode=0, dlPressureDirection=[0.0,0.0,0.0], crlTargets=[], crEdit=None)
```
