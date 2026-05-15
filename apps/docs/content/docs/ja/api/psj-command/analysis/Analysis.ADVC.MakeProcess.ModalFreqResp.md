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

<!-- @since:5.0.1 @required -->
### strName

- Specify the process name of ADVC - Modal Frequency Response process.

<!-- @since:5.0.1 @optional -->
### strRefEigenDir

- Specify the reference eigen direction which is the path of a folder.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### dRefLowFreq

- Specify the reference low frequency.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dRefHighFreq

- Specify the reference high frequency.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crModalDampingRatio

- Specify the modal damping ratio.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crExcitationFreq

- Specify the excitation frequency.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### bAutoFreqInterval

- Specify whether to enable the auto frequency interval or not.
  - If _True_: All settings of frequency interval will be able to use.
  - If _False_: All settings of frequency interval won't be able to use.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dMaxFreq

- Specify the maximum frequency.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMinFreq

- Specify the minimum frequency.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iNumFreqPoint

- Specify the number frequency point.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### dBiasParam

- Specify the bias parameter.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an ADVC Modal Frequency Response process.
  - If this parameter is used, the specified job will be modified.
  - If it is left _None_, a new job will be created.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### listLoadNode

- Specify the list of nodes that assigned loads in the model.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listLoadCaseNode

- Specify the list of nodes that assigned load cases in the model.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listLoadNodeContact

- Specify the list of nodes that assigned contacts in the model.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### ilOutputParamList

- Specify the list of output request for the result type such as Displacement, Stress, Strain,...
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iRefType

- Specify the result reference type.
  - If _iRefType=0_: Temperature Load
  - If _iRefType=1_: Stress
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strRefPath

- Specify the path of reference result.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### listAdvcRefStressResult

- Specify the list of data of Reference Result.
- The default value is \[].

## Return Code

A _Cursor_ specifying the newly created or the modified ADVC Modal Frequency Response process.

## Sample Code

```psj {3-4}
Geometry.Part.Cube()

process = Analysis.ADVC.MakeProcess.ModalFreqResp(strName="Process _0", listLoadNode=[],
    listLoadCaseNode=[], listLoadNodeContact=[], listAdvcRefStressResult=[])
print(str(process)) #for checking return value
```
