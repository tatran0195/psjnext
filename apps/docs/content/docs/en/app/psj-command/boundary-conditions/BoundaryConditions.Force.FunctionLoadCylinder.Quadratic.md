---
title: "BoundaryConditions.Force.FunctionLoadCylinder.Quadratic()"
description: "Create Force (Quadratic) y = a*x^2 + b"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Force > FunctionLoadCylinder > Quadratic"
---

## Description

Create Force (Quadratic) y = a\*x^2 + b.

## Syntax

```psj
BoundaryConditions.Force.FunctionLoadCylinder.Quadratic(...)
```

## Inputs

### `strName` @type(String) @default("ForceQuadratic1")

- The name.

### `dFTotalForce` @type(Double) @default(0.0)

- The total force.

### `dA` @type(Double) @default(0.0)

- The a.

### `dB` @type(Double) @default(0.0)

- The .

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `iAngleBase` @type(Integer) @default(0)

- The angle base.

### `dAngleRange` @type(Double) @default(0.0)

- The angle range.

### `iEnArrowDir` @type(Integer) @default(0)

- The en arrow direction.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Force.FunctionLoadCylinder.Quadratic(strName="ForceQuadratic1", dFTotalForce=0.0, dA=0.0, dB=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, crlTargets=[], crEdit=None)
```
