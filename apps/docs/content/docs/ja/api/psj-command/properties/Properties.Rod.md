---
title: "Properties.Rod()"
description: "create 1D rod property"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Rod"
macro _link: "[Property1DRod](../../macro/properties/Property1DRod)"
---

## Description

Create 1D rod property

## Syntax

```psj
Properties.Rod(strName="", iPID=1, crSection=None, crMat=None, dArea=DFLT _DBL, dTorConst=DFLT _DBL, dTorStressCoeff=DFLT _DBL, dNSM=DFLT _DBL, iLocalLengthUnit=0, iLocalMassUnit=0, crlTargets=[], crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iPID

- Specify the ID.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### crSection

- Specify the section.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crMat

- Specify the material.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dArea

- Specify the area.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTorConst

- Specify the tor const.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTorStressCoeff

- Specify the tor stress coeff.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNSM

- Specify the n s m.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iLocalLengthUnit

- Specify the local length unit.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iLocalMassUnit

- Specify the local mass unit.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Rod(strName="", iPID=1, crSection=None, crMat=None, dArea=DFLT _DBL, dTorConst=DFLT _DBL, dTorStressCoeff=DFLT _DBL, dNSM=DFLT _DBL, iLocalLengthUnit=0, iLocalMassUnit=0, crlTargets=[], crEdit=None)
```
