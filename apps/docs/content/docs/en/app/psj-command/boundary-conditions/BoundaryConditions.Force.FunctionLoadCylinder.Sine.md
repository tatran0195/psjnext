---
title: "BoundaryConditions.Force.FunctionLoadCylinder.Sine()"
description: "Define the force load on selected entity based on the distribution of the sine function"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Force > FunctionLoadCylinder > Sine"
---

## Description

Define the force load on selected entity based on the distribution of the sine function.

## Syntax

```psj
BoundaryConditions.Force.FunctionLoadCylinder.Sine(...)
```

## Inputs

### `strName` @type(String) @default("ForceSine1")

- The name.

### `dFTotalForce` @type(Double) @default(0.0)

- The total force.

### `dA` @type(Double) @default(0.0)

- The a.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `iAngleBase` @type(Integer) @default(0)

- The angle base.

### `dAngleRange` @type(Double) @default(0.0)

- The angle range.

### `iEnArrowDir` @type(Integer) @default(0)

- The en arrow direction.

### `bDistributeInAxis` @type(Boolean) @default(False)

- The distribute in axis.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Force.FunctionLoadCylinder.Sine(strName="ForceSine1", dFTotalForce=0.0, dA=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, bDistributeInAxis=False, crlTargets=[], crEdit=None)
```
