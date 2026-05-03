---
title: "StiffCalc.Force()"
description: "create NormalUnityForce"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "StiffCalc > Force"
---

## Description

Create NormalUnityForce

## Syntax

```psj
StiffCalc.Force(strName, poslForce, poslMoment, iEnArrowDir, iDistributionMethod, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula0, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, crlTargets, crEdit)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `poslForce` @type(Position List) @required

- The force.

### `poslMoment` @type(Position List) @required

- The moment.

### `iEnArrowDir` @type(Integer) @required

- The en arrow direction.

### `iDistributionMethod` @type(Integer) @required

- The distribution method.

### `crCurCoord` @type(Cursor) @required

- The cur coordinate.

### `crTable` @type(Cursor) @required

- The table.

### `crNodeSet` @type(Cursor) @required

- The node set.

### `dFPhase` @type(Double) @required

- The phase.

### `dFDelay` @type(Double) @required

- The delay.

### `crPhaseTable` @type(Cursor) @required

- The phase table.

### `strFormula0` @type(String) @required

- The formula0.

### `strFormula1` @type(String) @required

- The formula1.

### `strFormula2` @type(String) @required

- The formula2.

### `strFormula3` @type(String) @required

- The formula3.

### `strFormula4` @type(String) @required

- The formula4.

### `strFormula5` @type(String) @required

- The formula5.

### `crlTargets` @type(List\[Cursor]) @required

- The target.

### `crEdit` @type(Cursor) @required

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
StiffCalc.Force(strName, poslForce, poslMoment, iEnArrowDir, iDistributionMethod, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula0, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, crlTargets, crEdit)
```
