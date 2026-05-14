---
title: "Analysis.ADVC.MakeProcess.RandomResponse()"
description: "Create ADVC random response process"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ADVC > MakeProcess > RandomResponse"
macro _link: "[AdvcRandomProcess](../../macro/analysis/AdvcRandomProcess)"
---

## Description

Create ADVC random response process

## Syntax

```psj
Analysis.ADVC.MakeProcess.RandomResponse(...)
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

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crModalDampingRatio`

- The modal damping ratio.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crExcitationFreq`

- The excitation frequence.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bAutoFreqInterval`

- The auto frequence interval.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMaxFreq`

- The maximum frequence.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMinFreq`

- The minimum frequence.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNumFreqPoint`

- The number frequence point.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dBiasParam`

- The bias param.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPropMethod`

- The property method.

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iPSDtype`

- The PSD type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPSDdir`

- The PSD ddir.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crPSDLoad`

- The PSD load.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dPSDFactor`

- The PSD factor.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dGravityAccel`

- The gravity accel.

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iOutputEigenFreqStep`

- The output eigen frequence step.

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

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
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
Analysis.ADVC.MakeProcess.RandomResponse(strName="", strRefEigenDir="", dRefLowFreq=DFLT _DBL, dRefHighFreq=DFLT _DBL, crModalDampingRatio=None, crExcitationFreq=None, bAutoFreqInterval=False, dMaxFreq=DFLT _DBL, dMinFreq=DFLT _DBL, iNumFreqPoint=DFLT _INT, dBiasParam=DFLT _DBL, iPropMethod=0, iPSDtype=-1, iPSDdir=0, crPSDLoad=None, dPSDFactor=DFLT _DBL, dGravityAccel=DFLT _DBL, iOutputEigenFreqStep=-1, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```
