---
title: "Analysis.ADVC.MakeProcess.ModalFreqResp()"
description: "Create an ADVC Modal Frequency Response process. This process could be created in one time or multiple times"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ADVC > Structure > ModalFreqResp"
macro _link: "[AdvcModalFreqRespProcess](../../macro/analysis/AdvcModalFreqRespProcess)"
---

## Description

Create an ADVC Modal Frequency Response process.
This process could be created in one time or multiple times.

## Syntax

```psj
Analysis.ADVC.MakeProcess.ModalFreqResp(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The process name of ADVC - Modal Frequency Response process.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strRefEigenDir`

- The reference eigen direction which is the path of a folder.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dRefLowFreq`

- The reference low frequency.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dRefHighFreq`

- The reference high frequency.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crModalDampingRatio`

- The modal damping ratio.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crExcitationFreq`

- The excitation frequency.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bAutoFreqInterval`

- Whether to enable the auto frequency interval or not.
  - If _True_: All settings of frequency interval will be able to use.
  - If _False_: All settings of frequency interval won't be able to use.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMaxFreq`

- The maximum frequency.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMinFreq`

- The minimum frequency.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNumFreqPoint`

- The number frequency point.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dBiasParam`

- The bias parameter.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An ADVC Modal Frequency Response process.
  - If this parameter is used, the specified job will be modified.
  - If it is left _None_, a new job will be created.

<!-- @since:5.0.1 @type:List[ADVC _LOAD _NODE] @optional @default:[] -->
### `listLoadNode`

- The list of nodes that assigned loads in the model.

<!-- @since:5.0.1 @type:List[ADVC _LOAD _NODE] @optional @default:[] -->
### `listLoadCaseNode`

- The list of nodes that assigned load cases in the model.

<!-- @since:5.0.1 @type:List[ADVC _LOAD _NODE] @optional @default:[] -->
### `listLoadNodeContact`

- The list of nodes that assigned contacts in the model.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilOutputParamList`

- The list of output request for the result type such as Displacement, Stress, Strain,...

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iRefType`

- The result reference type.
  - If _iRefType=0_: Temperature Load
  - If _iRefType=1_: Stress

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strRefPath`

- The path of reference result.

<!-- @since:5.0.1 @type:List[ADVC _REF _STRESS _RESULT] @optional @default:[] -->
### `listAdvcRefStressResult`

- The list of data of Reference Result.

## Return Code

A _Cursor_ specifying the newly created or the modified ADVC Modal Frequency Response process.

## Sample Code

```psj {3-4}
Geometry.Part.Cube()

process = Analysis.ADVC.MakeProcess.ModalFreqResp(strName="Process _0", listLoadNode=[],
    listLoadCaseNode=[], listLoadNodeContact=[], listAdvcRefStressResult=[])
print(str(process)) #for checking return value
```
