---
title: "BoundaryConditions.Force.FunctionLoadCylinder.Vector()"
description: "Define the force load on selected entity based on the distribution of the vector function"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Force > FunctionLoadCylinder > Vector"
---

## Description

Define the force load on selected entity based on the distribution of the vector function.

## Syntax

```psj
BoundaryConditions.Force.FunctionLoadCylinder.Vector(...)
```

## Inputs

### `strName` @type(String) @default("ForceVector1")

- The name.

### `dFTotalForce` @type(Double) @default(DFLT\_DBL)

- The total force.

### `dA` @type(Double) @default(DFLT\_DBL)

- The a.

### `dX` @type(Double) @default(DFLT\_DBL)

- The x.

### `dY` @type(Double) @default(DFLT\_DBL)

- The y.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `iEnDirection` @type(Integer) @default(0)

- The en direction.

### `dAngleRange` @type(Double) @default(0.0)

- The angle range.

### `iArrowDir` @type(Integer) @default(0)

- The arrow direction.

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
BoundaryConditions.Force.FunctionLoadCylinder.Vector(strName="ForceVector1", dFTotalForce=DFLT_DBL, dA=DFLT_DBL, dX=DFLT_DBL, dY=DFLT_DBL, crCoord=None, iEnDirection=0, dAngleRange=0.0, iArrowDir=0, bDistributeInAxis=False, crlTargets=[], crEdit=None)
```
