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

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strDesp`

- The description.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableAutomatic`

- The enable automatic.

<!-- @since:5.0.1 @type:Integer @optional @default:100 -->
### `iMaxInc`

- The maximum increment.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dInitSize`

- The initial size.

<!-- @since:5.0.1 @type:Double @optional @default:1.0e-5 -->
### `dMinSize`

- The minimum size.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dMaxSize`

- The maximum size.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMatrixStorage`

- The matrix storage.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMaxLdPropFactor`

- The maximum ld property factor.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableMaxLdPropFactor`

- The enable maximum ld property factor.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableMaxDisp`

- The enable maximum displacement.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMaxDisp`

- The maximum displacement.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iEnableMaxDispDof`

- The enable maximum displacement dof.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strNdRgn`

- The nd rgn.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableNlgeom`

- The enable nlgeom.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableIncludeHeatEffect`

- The enable include heat effect.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iConvertDscntIter`

- The convert destination count iterator.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dTotalArcLength`

- The total arc length.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iExtrapolateMethod`

- The extrapolate method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableAcceptByMaxIters`

- The enable accept by maximum iterators.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableLongTerm`

- The enable long term.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnablePerturbation`

- The enable perturbation.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFullplasticregionBchecked`

- The fullplasticregion check.

<!-- @since:5.0.1 @type:List[String] @optional @default:[] -->
### `strlFullplasticregionTlist`

- The fullplasticregion table list.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iOutput`

- The output.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

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
