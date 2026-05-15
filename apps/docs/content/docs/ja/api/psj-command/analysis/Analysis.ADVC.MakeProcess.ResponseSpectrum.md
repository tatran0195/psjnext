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
### iPropMethod

- Specify the property method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSpttype

- Specify the spectrum type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSptFactor0

- Specify the spectrum factor0.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crSpt0

- Specify the spt0.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dSptFactor1

- Specify the spectrum factor1.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crSpt1

- Specify the spectrum 1.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dSptFactor2

- Specify the spectrum factor2.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crSpt2

- Specify the spectrum 2.
- The default value is None.

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
- The default value is 0.

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
Analysis.ADVC.MakeProcess.ResponseSpectrum(strName="", strRefEigenDir="", dRefLowFreq=DFLT _DBL, dRefHighFreq=DFLT _DBL, iPropMethod=0, iSpttype=0, dSptFactor0=DFLT _DBL, crSpt0=None, dSptFactor1=DFLT _DBL, crSpt1=None, dSptFactor2=DFLT _DBL, crSpt2=None, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=0, strRefPath="", listAdvcRefStressResult=[])
```
