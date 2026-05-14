---
title: "StiffCalc.Force()"
description: "create NormalUnityForce"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "StiffCalc > Force"
---

## Description

Create NormalUnityForce

## Syntax

```psj
StiffCalc.Force(strName, poslForce, poslMoment, iEnArrowDir, iDistributionMethod, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula0, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, crlTargets, crEdit)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Position List @required -->
### `poslForce`

- The force.

<!-- @since:5.0.1 @type:Position List @required -->
### `poslMoment`

- The moment.

<!-- @since:5.0.1 @type:Integer @required -->
### `iEnArrowDir`

- The en arrow direction.

<!-- @since:5.0.1 @type:Integer @required -->
### `iDistributionMethod`

- The distribution method.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crCurCoord`

- The cur coordinate.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crTable`

- The table.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crNodeSet`

- The node set.

<!-- @since:5.0.1 @type:Double @required -->
### `dFPhase`

- The phase.

<!-- @since:5.0.1 @type:Double @required -->
### `dFDelay`

- The delay.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crPhaseTable`

- The phase table.

<!-- @since:5.0.1 @type:String @required -->
### `strFormula0`

- The formula0.

<!-- @since:5.0.1 @type:String @required -->
### `strFormula1`

- The formula1.

<!-- @since:5.0.1 @type:String @required -->
### `strFormula2`

- The formula2.

<!-- @since:5.0.1 @type:String @required -->
### `strFormula3`

- The formula3.

<!-- @since:5.0.1 @type:String @required -->
### `strFormula4`

- The formula4.

<!-- @since:5.0.1 @type:String @required -->
### `strFormula5`

- The formula5.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
StiffCalc.Force(strName, poslForce, poslMoment, iEnArrowDir, iDistributionMethod, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula0, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, crlTargets, crEdit)
```
