---
title: 'Analysis.ADVC.MakeProcess.ModalFreqResp()'
description: 'Create an ADVC Modal Frequency Response process. This process could be created in one time or multiple times'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > ADVC > Structure > ModalFreqResp'
macro_link: '[AdvcModalFreqRespProcess](../../macro/analysis/AdvcModalFreqRespProcess)'
---

## Description

Create an ADVC Modal Frequency Response process.
This process could be created in one time or multiple times.

## Syntax

```psj
Analysis.ADVC.MakeProcess.ModalFreqResp(...)
```

## Inputs

### `strName` @type(String) @required

- The process name of ADVC - Modal Frequency Response process.

### `strRefEigenDir` @type(String) @default("")

- The reference eigen direction which is the path of a folder.

### `dRefLowFreq` @type(Double) @default(DFLT_DBL)

- The reference low frequency.

### `dRefHighFreq` @type(Double) @default(DFLT_DBL)

- The reference high frequency.

### `crModalDampingRatio` @type(Cursor) @default(None)

- The modal damping ratio.

### `crExcitationFreq` @type(Cursor) @default(None)

- The excitation frequency.

### `bAutoFreqInterval` @type(Boolean) @default(False)

- Whether to enable the auto frequency interval or not.
    - I&#x66;_&#x54;rue_: All settings of frequency interval will be able to use.
    - I&#x66;_&#x46;alse_: All settings of frequency interval won't be able to use.

### `dMaxFreq` @type(Double) @default(DFLT_DBL)

- The maximum frequency.

### `dMinFreq` @type(Double) @default(DFLT_DBL)

- The minimum frequency.

### `iNumFreqPoint` @type(Integer) @default(DFLT_INT)

- The number frequency point.

### `dBiasParam` @type(Double) @default(DFLT_DBL)

- The bias parameter.

### `crEdit` @type(Cursor) @default(None)

- An ADVC Modal Frequency Response process.
    - If this parameter is used, the specified job will be modified.
    - If it is lef&#x74;_&#x4E;one_, a new job will be created.

### `listLoadNode` @type(List\[ADVC_LOAD_NODE]) @default(\[])

- The list of nodes that assigned loads in the model.

### `listLoadCaseNode` @type(List\[ADVC_LOAD_NODE]) @default(\[])

- The list of nodes that assigned load cases in the model.

### `listLoadNodeContact` @type(List\[ADVC_LOAD_NODE]) @default(\[])

- The list of nodes that assigned contacts in the model.

### `ilOutputParamList` @type(List\[Integer]) @default(\[])

- The list of output request for the result type such as Displacement, Stress, Strain,...

### `iRefType` @type(Integer) @default(0)

- The result reference type.
    - I&#x66;_&#x69;RefType=0_: Temperature Load
    - I&#x66;_&#x69;RefType=1_: Stress

### `strRefPath` @type(String) @default("")

- The path of reference result.

### `listAdvcRefStressResult` @type(List\[ADVC_REF_STRESS_RESULT]) @default(\[])

- The list of data of Reference Result.

## Return Code

A _Cursor_ specifying the newly created or the modified ADVC Modal Frequency Response process.

## Sample Code

```psj {3-4}
Geometry.Part.Cube()

process = Analysis.ADVC.MakeProcess.ModalFreqResp(strName="Process_0", listLoadNode=[],
    listLoadCaseNode=[], listLoadNodeContact=[], listAdvcRefStressResult=[])
print(str(process)) #for checking return value
```
