---
title: "BoundaryConditions.Pressure.FunctionLoadToCylinderSine()"
description: "Define a pressure load on the selected face or element surface based on a sine function distribution."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Pressure > FunctionLoadToCylinderSine"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Define a pressure load on the selected face or element surface based on a sine function distribution."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Define a pressure load on the selected face or element surface based on a sine function distribution.

## Syntax

```psj
BoundaryConditions.Pressure.FunctionLoadToCylinderSine(...)
```

## Inputs

### `strName` @type(String) @default("PressureSine1")

- The name.

### `dA` @type(Double) @default(0.0)

- The a.

### `crCoordinate` @type(Cursor) @default(None)

- The coordinate.

### `dAngleRange` @type(Double) @default(0.0)

- The angle range.

### `bDistributionAxis` @type(Boolean) @default(False)

- The distribution axis.

### `iPressureDirectionMode` @type(Integer) @default(0)

- The pressure direction mode.

### `bIsTotalForceAdjustment` @type(Boolean) @default(False)

- The is total force adjustment.

### `dTotalForce` @type(Double) @default(0.0)

- The total force.

### `vecPressureDirection` @type(Vector) @default(\[0.0,0.0,0.0])

- The pressure direction.

### `crCoordinateSystemForDirection` @type(Cursor) @default(None)

- The coordinate system for direction.

### `bIsCornerNodesDistribution` @type(Boolean) @default(False)

- The is corner nodes distribution.

### `strFormulaForA` @type(String) @default("")

- The formula for a.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Pressure.FunctionLoadToCylinderSine(strName="PressureSine1", dA=0.0, crCoordinate=None, dAngleRange=0.0, bDistributionAxis=False, iPressureDirectionMode=0, bIsTotalForceAdjustment=False, dTotalForce=0.0, vecPressureDirection=[0.0,0.0,0.0], crCoordinateSystemForDirection=None, bIsCornerNodesDistribution=False, strFormulaForA="", crlTargets=[], crEdit=None)
```
