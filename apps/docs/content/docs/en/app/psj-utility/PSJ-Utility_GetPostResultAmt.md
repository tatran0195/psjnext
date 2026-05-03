---
title: "JPT.GetPostResultAmt()"
description: "Get Physical Amount information of the specify result"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get Physical Amount information of the specify result.

## Syntax

```psj
JPT.GetPostResultAmt(PostAnalysisType,
                     resultSet,
                     timeStep,
                     resultName,
                     componentName,
                     PostResultDataLoc)
```

## Inputs

### `PostAnalysisType` @type(Enum) @required

- Th&#x65;_[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_&#x64;escribing the type of analysis result.

### `resultSet` @type(Integer) @required

- The step ID of the imported result.

### `timeStep` @type(Integer) @required

- The time step of the imported result.

### `resultName` @type(String) @required

- The type of result (Such as Displacement, Stress, etc.).

### `componentName` @type(String) @required

- A specific direction of the result (Such as X, Y, Z, etc.).

### `PostResultDataLoc` @type(Enum) @required

- Th&#x65;_[PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types)_&#x64;escribing the location of result (Such as on node, on element, etc.).

## Return Code

An _Integer_ specifying the [Physical Amount](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-amt-types) type of the working result.

## Sample Code

```psj {6-11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, \
                               1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

amt_info = JPT.GetPostResultAmt(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                               1,
                               1,
                               "Stress",
                               "XX",
                               JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE)
JPT.Debugger(amt_info)
```
