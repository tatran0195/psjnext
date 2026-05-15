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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### strRefEigenDir

- Specify the reference eigen direction.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### dRefLowFreq

- Specify the reference low frequence.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dRefHighFreq

- Specify the reference high frequence.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crModalDampingRatio

- Specify the modal damping ratio.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crExcitationFreq

- Specify the excitation frequence.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### bAutoFreqInterval

- Specify the auto frequence interval.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dMaxFreq

- Specify the maximum frequence.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMinFreq

- Specify the minimum frequence.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iNumFreqPoint

- Specify the number frequence point.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### dBiasParam

- Specify the bias param.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iPropMethod

- Specify the property method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPSDtype

- Specify the PSD type.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### iPSDdir

- Specify the PSD ddir.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crPSDLoad

- Specify the PSD load.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dPSDFactor

- Specify the PSD factor.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dGravityAccel

- Specify the gravity accel.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iOutputEigenFreqStep

- Specify the output eigen frequence step.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### listLoadNode

- Specify the load node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listLoadCaseNode

- Specify the load case node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listLoadNodeContact

- Specify the load node contact.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### ilOutputParamList

- Specify the output param list.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iRefType

- Specify the reference type.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### strRefPath

- Specify the reference path.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### listAdvcRefStressResult

- Specify the advc reference stress result.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.ADVC.MakeProcess.RandomResponse(strName="", strRefEigenDir="", dRefLowFreq=DFLT _DBL, dRefHighFreq=DFLT _DBL, crModalDampingRatio=None, crExcitationFreq=None, bAutoFreqInterval=False, dMaxFreq=DFLT _DBL, dMinFreq=DFLT _DBL, iNumFreqPoint=DFLT _INT, dBiasParam=DFLT _DBL, iPropMethod=0, iPSDtype=-1, iPSDdir=0, crPSDLoad=None, dPSDFactor=DFLT _DBL, dGravityAccel=DFLT _DBL, iOutputEigenFreqStep=-1, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```
