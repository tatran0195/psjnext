---
title: "Connections.SpringsDampers.BushGeneral()"
description: "Create bush connection"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > SpringsDampers > BushGeneral"
macro_link: "[Bush](../../macro/connections/Bush)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Create bush connection"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create bush connection

## Syntax

```psj
Connections.SpringsDampers.BushGeneral(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
```

## Inputs

### `iMethod` @type(Integer) @required

- The method.

### `strName` @type(String) @required

- The name.

### `crlMaster` @type(List\[Cursor]) @required

- The master.

### `crlSlave` @type(List\[Cursor]) @required

- The slave.

### `crCoord` @type(Cursor) @required

- The coordinate.

### `dTol` @type(Double) @required

- The tolerance.

### `iGround` @type(Integer) @required

- The ground.

### `iOriMode` @type(Integer) @required

- The ori mode.

### `iEqual` @type(Integer) @required

- The equal.

### `poslVector` @type(Position List) @required

- The vector.

### `dlStiffness` @type(Double List) @required

- The stiffness.

### `dlDampCoef` @type(Double List) @required

- The damp coefficient .

### `dlDampConst` @type(Double List) @required

- The damp const.

### `dRotStrain` @type(Double) @required

- The rotation strain.

### `dTransStrain` @type(Double) @required

- The trans strain.

### `dRotStress` @type(Double) @required

- The rotation stress.

### `dTransStress` @type(Double) @required

- The trans stress.

### `crEditObj` @type(Cursor) @required

- The edit object.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.SpringsDampers.BushGeneral(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
```
