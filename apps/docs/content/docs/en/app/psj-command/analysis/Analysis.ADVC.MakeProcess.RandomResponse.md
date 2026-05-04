---
title: 'Analysis.ADVC.MakeProcess.RandomResponse()'
description: 'Create ADVC random response process'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > ADVC > MakeProcess > RandomResponse'
macro_link: '[AdvcRandomProcess](../../macro/analysis/AdvcRandomProcess)'
---

## Description

Create ADVC random response process

## Syntax

```psj
Analysis.ADVC.MakeProcess.RandomResponse(...)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `strRefEigenDir` @type(String) @default("")

- The reference eigen direction.

### `dRefLowFreq` @type(Double) @default(DFLT_DBL)

- The reference low frequence.

### `dRefHighFreq` @type(Double) @default(DFLT_DBL)

- The reference high frequence.

### `crModalDampingRatio` @type(Cursor) @default(None)

- The modal damping ratio.

### `crExcitationFreq` @type(Cursor) @default(None)

- The excitation frequence.

### `bAutoFreqInterval` @type(Boolean) @default(False)

- The auto frequence interval.

### `dMaxFreq` @type(Double) @default(DFLT_DBL)

- The maximum frequence.

### `dMinFreq` @type(Double) @default(DFLT_DBL)

- The minimum frequence.

### `iNumFreqPoint` @type(Integer) @default(DFLT_INT)

- The number frequence point.

### `dBiasParam` @type(Double) @default(DFLT_DBL)

- The bias param.

### `iPropMethod` @type(Integer) @default(0)

- The property method.

### `iPSDtype` @type(Integer) @default(-1)

- The PSD type.

### `iPSDdir` @type(Integer) @default(0)

- The PSD ddir.

### `crPSDLoad` @type(Cursor) @default(None)

- The PSD load.

### `dPSDFactor` @type(Double) @default(DFLT_DBL)

- The PSD factor.

### `dGravityAccel` @type(Double) @default(DFLT_DBL)

- The gravity accel.

### `iOutputEigenFreqStep` @type(Integer) @default(-1)

- The output eigen frequence step.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `listLoadNode` @type(LOAD_NODE List) @default(\[])

- The load node.

### `listLoadCaseNode` @type(LOAD_CASE_NODE List) @default(\[])

- The load case node.

### `listLoadNodeContact` @type(LOAD_NODE_CONTACT List) @default(\[])

- The load node contact.

### `ilOutputParamList` @type(List\[Integer]) @default(\[])

- The output param list.

### `iRefType` @type(Integer) @default(-1)

- The reference type.

### `strRefPath` @type(String) @default("")

- The reference path.

### `listAdvcRefStressResult` @type(ADVC_REF_STRESS_RESULT List) @default(\[])

- The advc reference stress result.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.ADVC.MakeProcess.RandomResponse(strName="", strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, crModalDampingRatio=None, crExcitationFreq=None, bAutoFreqInterval=False, dMaxFreq=DFLT_DBL, dMinFreq=DFLT_DBL, iNumFreqPoint=DFLT_INT, dBiasParam=DFLT_DBL, iPropMethod=0, iPSDtype=-1, iPSDdir=0, crPSDLoad=None, dPSDFactor=DFLT_DBL, dGravityAccel=DFLT_DBL, iOutputEigenFreqStep=-1, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```
