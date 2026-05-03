---
title: "Analysis.ADVC.MakeProcess.ResponseSpectrum()"
description: "Create advc response spectrum process"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > ADVC > MakeProcess > ResponseSpectrum"
macro_link: "[AdvcSpectrumProcess](../../macro/analysis/AdvcSpectrumProcess)"
---

## Description

Create advc response spectrum process.

## Syntax

```psj
Analysis.ADVC.MakeProcess.ResponseSpectrum(...)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `strRefEigenDir` @type(String) @default("")

- The reference eigen direction.

### `dRefLowFreq` @type(Double) @default(DFLT\_DBL)

- The reference low frequence.

### `dRefHighFreq` @type(Double) @default(DFLT\_DBL)

- The reference high frequence.

### `iPropMethod` @type(Integer) @default(0)

- The property method.

### `iSpttype` @type(Integer) @default(0)

- The spectrum type.

### `dSptFactor0` @type(Double) @default(DFLT\_DBL)

- The spectrum factor0.

### `crSpt0` @type(Cursor) @default(None)

- The spt0.

### `dSptFactor1` @type(Double) @default(DFLT\_DBL)

- The spectrum factor1.

### `crSpt1` @type(Cursor) @default(None)

- The spectrum 1.

### `dSptFactor2` @type(Double) @default(DFLT\_DBL)

- The spectrum factor2.

### `crSpt2` @type(Cursor) @default(None)

- The spectrum 2.

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

### `iRefType` @type(Integer) @default(0)

- The reference type.

### `strRefPath` @type(String) @default("")

- The reference path.

### `listAdvcRefStressResult` @type(ADVC\_REF\_STRESS\_RESULT List) @default(\[])

- The advc reference stress result.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.ADVC.MakeProcess.ResponseSpectrum(strName="", strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, iPropMethod=0, iSpttype=0, dSptFactor0=DFLT_DBL, crSpt0=None, dSptFactor1=DFLT_DBL, crSpt1=None, dSptFactor2=DFLT_DBL, crSpt2=None, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=0, strRefPath="", listAdvcRefStressResult=[])
```
