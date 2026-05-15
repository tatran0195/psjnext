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

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### poslForce

- Specify the force.

<!-- @since:5.0.1 @required -->
### poslMoment

- Specify the moment.

<!-- @since:5.0.1 @required -->
### iEnArrowDir

- Specify the en arrow direction.

<!-- @since:5.0.1 @required -->
### iDistributionMethod

- Specify the distribution method.

<!-- @since:5.0.1 @required -->
### crCurCoord

- Specify the cur coordinate.

<!-- @since:5.0.1 @required -->
### crTable

- Specify the table.

<!-- @since:5.0.1 @required -->
### crNodeSet

- Specify the node set.

<!-- @since:5.0.1 @required -->
### dFPhase

- Specify the phase.

<!-- @since:5.0.1 @required -->
### dFDelay

- Specify the delay.

<!-- @since:5.0.1 @required -->
### crPhaseTable

- Specify the phase table.

<!-- @since:5.0.1 @required -->
### strFormula0

- Specify the formula0.

<!-- @since:5.0.1 @required -->
### strFormula1

- Specify the formula1.

<!-- @since:5.0.1 @required -->
### strFormula2

- Specify the formula2.

<!-- @since:5.0.1 @required -->
### strFormula3

- Specify the formula3.

<!-- @since:5.0.1 @required -->
### strFormula4

- Specify the formula4.

<!-- @since:5.0.1 @required -->
### strFormula5

- Specify the formula5.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the target.

<!-- @since:5.0.1 @required -->
### crEdit

- Specify the edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
StiffCalc.Force(strName, poslForce, poslMoment, iEnArrowDir, iDistributionMethod, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula0, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, crlTargets, crEdit)
```
