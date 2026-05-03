---
title: "Analysis.ADVC.MakeProcess.Fatigue()"
description: "Create ADVC fatigue process"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > ADVC > MakeProcess > Fatigue"
macro_link: "[AdvcFatigueProcess](../../macro/analysis/AdvcFatigueProcess)"
---

## Description

Create ADVC fatigue process.

## Syntax

```psj
Analysis.ADVC.MakeProcess.Fatigue(...)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `bFatigue` @type(Boolean) @default(False)

- The fatigue.

### `iMethod` @type(Integer) @default(0)

- The method.

### `iStressAxis` @type(Integer) @default(0)

- The stress axis.

### `iSafetyType` @type(Integer) @default(0)

- The safety type.

### `dSearchResolution` @type(Double) @default(DFLT\_DBL)

- The search resolution.

### `dSafetyMax` @type(Double) @default(DFLT\_DBL)

- The safety maximum.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `listLoadNode` @type(LOAD\_NODE List) @default(\[])

- The load node.

### `listLoadCaseNode` @type(LOAD\_CASE\_NODE List) @default(\[])

- The load case node.

### `listLoadNodeContact` @type(LOAD\_NODE\_CONTACT List) @default(\[])

- The load node contact.

### `ilOutputParamList` @type(List\[Integer]) @default(\[])

- The output param list.

### `iRefType` @type(Integer) @default(-1)

- The reference type.

### `strRefPath` @type(String) @default("")

- The reference path.

### `listAdvcRefStressResult` @type(ADVC\_REF\_STRESS\_RESULT List) @default(\[])

- The advc reference stress result.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.ADVC.MakeProcess.Fatigue(strName="", bFatigue=False, iMethod=0, iStressAxis=0, iSafetyType=0, dSearchResolution=DFLT_DBL, dSafetyMax=DFLT_DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```
