---
title: "Properties.Rod()"
description: "create 1D rod property"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Rod"
macro_link: "[Property1DRod](../../macro/properties/Property1DRod)"
---

## Description

Create 1D rod property

## Syntax

```psj
Properties.Rod(strName="", iPID=1, crSection=None, crMat=None, dArea=DFLT_DBL, dTorConst=DFLT_DBL, dTorStressCoeff=DFLT_DBL, dNSM=DFLT_DBL, iLocalLengthUnit=0, iLocalMassUnit=0, crlTargets=[], crEdit=None)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `iPID` @type(Integer) @default(1)

- The ID.

### `crSection` @type(Cursor) @default(None)

- The section.

### `crMat` @type(Cursor) @default(None)

- The material.

### `dArea` @type(Double) @default(DFLT\_DBL)

- The area.

### `dTorConst` @type(Double) @default(DFLT\_DBL)

- The tor const.

### `dTorStressCoeff` @type(Double) @default(DFLT\_DBL)

- The tor stress coeff.

### `dNSM` @type(Double) @default(DFLT\_DBL)

- The n s m.

### `iLocalLengthUnit` @type(Integer) @default(0)

- The local length unit.

### `iLocalMassUnit` @type(Integer) @default(0)

- The local mass unit.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Rod(strName="", iPID=1, crSection=None, crMat=None, dArea=DFLT_DBL, dTorConst=DFLT_DBL, dTorStressCoeff=DFLT_DBL, dNSM=DFLT_DBL, iLocalLengthUnit=0, iLocalMassUnit=0, crlTargets=[], crEdit=None)
```
