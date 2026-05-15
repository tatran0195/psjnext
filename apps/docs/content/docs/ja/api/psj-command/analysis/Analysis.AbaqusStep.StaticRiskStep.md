---
title: "Analysis.AbaqusStep.StaticRiskStep()"
description: "Abaqus Static Risk Step"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > AbaqusStep > StaticRiskStep"
---

## Description

Abaqus Static Risk Step

## Syntax

```psj
Analysis.AbaqusStep.StaticRiskStep(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @optional -->
### strDesp

- Specify the description.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iEnableAutomatic

- Specify the enable automatic.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMaxInc

- Specify the maximum increment.
- The default value is 100.

<!-- @since:5.0.1 @optional -->
### dInitSize

- Specify the initial size.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### dMinSize

- Specify the minimum size.
- The default value is 1.0e-5.

<!-- @since:5.0.1 @optional -->
### dMaxSize

- Specify the maximum size.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMatrixStorage

- Specify the matrix storage.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMaxLdPropFactor

- Specify the maximum ld property factor.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iEnableMaxLdPropFactor

- Specify the enable maximum ld property factor.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnableMaxDisp

- Specify the enable maximum displacement.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMaxDisp

- Specify the maximum displacement.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iEnableMaxDispDof

- Specify the enable maximum displacement dof.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### strNdRgn

- Specify the nd rgn.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iEnableNlgeom

- Specify the enable nlgeom.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnableIncludeHeatEffect

- Specify the enable include heat effect.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iConvertDscntIter

- Specify the convert destination count iterator.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTotalArcLength

- Specify the total arc length.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### iExtrapolateMethod

- Specify the extrapolate method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnableAcceptByMaxIters

- Specify the enable accept by maximum iterators.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnableLongTerm

- Specify the enable long term.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnablePerturbation

- Specify the enable perturbation.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iFullplasticregionBchecked

- Specify the fullplasticregion check.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strlFullplasticregionTlist

- Specify the fullplasticregion table list.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iOutput

- Specify the output.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.AbaqusStep.StaticRiskStep(strName, strDesp="", iEnableAutomatic=0, iMaxInc=100, dInitSize=1.0,
    dMinSize=1.0e-5, dMaxSize=1.0, iMethod=0, iMatrixStorage=0, dMaxLdPropFactor=0.0, iEnableMaxLdPropFactor=0,
    iEnableMaxDisp=0, dMaxDisp=DFLT _DBL, iEnableMaxDispDof=DFLT _INT, strNdRgn="", iEnableNlgeom=0,
    iEnableIncludeHeatEffect=0, iConvertDscntIter=0, dTotalArcLength=1.0, iExtrapolateMethod=0,
    iEnableAcceptByMaxIters=0, iEnableLongTerm=0, iEnablePerturbation=0, iFullplasticregionBchecked=0,
    strlFullplasticregionTlist=[], iOutput=0, crEdit=None)
```
