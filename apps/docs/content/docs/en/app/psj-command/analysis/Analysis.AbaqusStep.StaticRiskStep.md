---
title: "Analysis.AbaqusStep.StaticRiskStep()"
description: "Abaqus Static Risk Step"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > AbaqusStep > StaticRiskStep"
---

## Description

Abaqus Static Risk Step

## Syntax

```psj
Analysis.AbaqusStep.StaticRiskStep(...)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `strDesp` @type(String) @default("")

- The description.

### `iEnableAutomatic` @type(Integer) @default(0)

- The enable automatic.

### `iMaxInc` @type(Integer) @default(100)

- The maximum increment.

### `dInitSize` @type(Double) @default(1.0)

- The initial size.

### `dMinSize` @type(Double) @default(1.0e-5)

- The minimum size.

### `dMaxSize` @type(Double) @default(1.0)

- The maximum size.

### `iMethod` @type(Integer) @default(0)

- The method.

### `iMatrixStorage` @type(Integer) @default(0)

- The matrix storage.

### `dMaxLdPropFactor` @type(Double) @default(0.0)

- The maximum ld property factor.

### `iEnableMaxLdPropFactor` @type(Integer) @default(0)

- The enable maximum ld property factor.

### `iEnableMaxDisp` @type(Integer) @default(0)

- The enable maximum displacement.

### `dMaxDisp` @type(Double) @default(DFLT\_DBL)

- The maximum displacement.

### `iEnableMaxDispDof` @type(Integer) @default(DFLT\_INT)

- The enable maximum displacement dof.

### `strNdRgn` @type(String) @default("")

- The nd rgn.

### `iEnableNlgeom` @type(Integer) @default(0)

- The enable nlgeom.

### `iEnableIncludeHeatEffect` @type(Integer) @default(0)

- The enable include heat effect.

### `iConvertDscntIter` @type(Integer) @default(0)

- The convert destination count iterator.

### `dTotalArcLength` @type(Double) @default(1.0)

- The total arc length.

### `iExtrapolateMethod` @type(Integer) @default(0)

- The extrapolate method.

### `iEnableAcceptByMaxIters` @type(Integer) @default(0)

- The enable accept by maximum iterators.

### `iEnableLongTerm` @type(Integer) @default(0)

- The enable long term.

### `iEnablePerturbation` @type(Integer) @default(0)

- The enable perturbation.

### `iFullplasticregionBchecked` @type(Integer) @default(0)

- The fullplasticregion check.

### `strlFullplasticregionTlist` @type(List\[String]) @default(\[])

- The fullplasticregion table list.

### `iOutput` @type(Integer) @default(0)

- The output.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.AbaqusStep.StaticRiskStep(strName, strDesp="", iEnableAutomatic=0, iMaxInc=100, dInitSize=1.0,
    dMinSize=1.0e-5, dMaxSize=1.0, iMethod=0, iMatrixStorage=0, dMaxLdPropFactor=0.0, iEnableMaxLdPropFactor=0,
    iEnableMaxDisp=0, dMaxDisp=DFLT_DBL, iEnableMaxDispDof=DFLT_INT, strNdRgn="", iEnableNlgeom=0,
    iEnableIncludeHeatEffect=0, iConvertDscntIter=0, dTotalArcLength=1.0, iExtrapolateMethod=0,
    iEnableAcceptByMaxIters=0, iEnableLongTerm=0, iEnablePerturbation=0, iFullplasticregionBchecked=0,
    strlFullplasticregionTlist=[], iOutput=0, crEdit=None)
```
