---
title: "Analysis.ADVC.MakeProcess.ResponseSpectrum()"
description: "Create advc response spectrum process"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ADVC > MakeProcess > ResponseSpectrum"
macro _link: "[AdvcSpectrumProcess](../../macro/analysis/AdvcSpectrumProcess)"
---

## Description

Create advc response spectrum process.

## Syntax

```psj
Analysis.ADVC.MakeProcess.ResponseSpectrum(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strRefEigenDir`

- The reference eigen direction.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dRefLowFreq`

- The reference low frequence.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dRefHighFreq`

- The reference high frequence.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPropMethod`

- The property method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSpttype`

- The spectrum type.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSptFactor0`

- The spectrum factor0.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crSpt0`

- The spt0.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSptFactor1`

- The spectrum factor1.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crSpt1`

- The spectrum 1.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSptFactor2`

- The spectrum factor2.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crSpt2`

- The spectrum 2.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:LOAD _NODE List @optional @default:[] -->
### `listLoadNode`

- The load node.

<!-- @since:5.0.1 @type:LOAD _CASE _NODE List @optional @default:[] -->
### `listLoadCaseNode`

- The load case node.

<!-- @since:5.0.1 @type:LOAD _NODE _CONTACT List @optional @default:[] -->
### `listLoadNodeContact`

- The load node contact.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilOutputParamList`

- The output param list.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iRefType`

- The reference type.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strRefPath`

- The reference path.

<!-- @since:5.0.1 @type:ADVC _REF _STRESS _RESULT List @optional @default:[] -->
### `listAdvcRefStressResult`

- The advc reference stress result.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.ADVC.MakeProcess.ResponseSpectrum(strName="", strRefEigenDir="", dRefLowFreq=DFLT _DBL, dRefHighFreq=DFLT _DBL, iPropMethod=0, iSpttype=0, dSptFactor0=DFLT _DBL, crSpt0=None, dSptFactor1=DFLT _DBL, crSpt1=None, dSptFactor2=DFLT _DBL, crSpt2=None, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=0, strRefPath="", listAdvcRefStressResult=[])
```
