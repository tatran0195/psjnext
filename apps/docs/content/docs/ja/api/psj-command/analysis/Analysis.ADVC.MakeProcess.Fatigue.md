---
title: "Analysis.ADVC.MakeProcess.Fatigue()"
description: "Create ADVC fatigue process"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ADVC > MakeProcess > Fatigue"
macro _link: "[AdvcFatigueProcess](../../macro/analysis/AdvcFatigueProcess)"
---

## Description

Create ADVC fatigue process.

## Syntax

```psj
Analysis.ADVC.MakeProcess.Fatigue(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### bFatigue

- Specify the fatigue.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iStressAxis

- Specify the stress axis.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSafetyType

- Specify the safety type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSearchResolution

- Specify the search resolution.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dSafetyMax

- Specify the safety maximum.
- The default value is DFLT\_DBL.

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
Analysis.ADVC.MakeProcess.Fatigue(strName="", bFatigue=False, iMethod=0, iStressAxis=0, iSafetyType=0, dSearchResolution=DFLT _DBL, dSafetyMax=DFLT _DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```
