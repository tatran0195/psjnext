---
title: "BoundaryConditions.InitialElementalValue.InitialStress()"
description: "Create mapping stress"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > InitialElementalValue > InitialStress"
---

## Description

Create mapping stress.

## Syntax

```psj
BoundaryConditions.InitialElementalValue.InitialStress(...)
```

## Inputs

### `strName` @type(String) @default("InitialStress1")

- The name.

### `iDimension` @type(Integer) @default(2)

- The dimension.

### `iElemCs` @type(Integer) @default(0)

- The element cs.

### `dSXX` @type(Double) @default(DFLT\_DBL)

- The s x x.

### `dSYY` @type(Double) @default(DFLT\_DBL)

- The s y y.

### `dSXY` @type(Double) @default(DFLT\_DBL)

- The s x y.

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
BoundaryConditions.InitialElementalValue.InitialStress(strName="InitialStress1", iDimension=2, iElemCs=0, dSXX=DFLT_DBL, dSYY=DFLT_DBL, dSXY=DFLT_DBL, crTable=None, crlTargets=[], crEdit=None)
```
