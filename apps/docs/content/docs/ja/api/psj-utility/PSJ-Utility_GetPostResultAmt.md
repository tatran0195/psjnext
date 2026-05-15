---
title: "JPT.GetPostResultAmt()"
description: "Get Physical Amount information of the specify result"
version _introduced: "5.0.1"
available _versions: "all"
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

<!-- @since:5.0.1 @required -->
### PostAnalysisType

- Specify the_[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.

<!-- @since:5.0.1 @required -->
### resultSet

- Specify the step ID of the imported result.

<!-- @since:5.0.1 @required -->
### timeStep

- Specify the time step of the imported result.

<!-- @since:5.0.1 @required -->
### resultName

- Specify the type of result (Such as Displacement, Stress, etc.).

<!-- @since:5.0.1 @required -->
### componentName

- Specify a specific direction of the result (Such as X, Y, Z, etc.).

<!-- @since:5.0.1 @required -->
### PostResultDataLoc

- Specify the_[PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types)_ describing the location of result (Such as on node, on element, etc.).

## Return Code

An _Integer_ specifying the [Physical Amount](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-amt-types) type of the working result.

## Sample Code

```psj {6-11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, \
                               1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

amt _info = JPT.GetPostResultAmt(JPT.PostAnalysisType.POST _ANALYSIS _LINEAR _STATIC,
                               1,
                               1,
                               "Stress",
                               "XX",
                               JPT.PostResultDataLoc.POST _LOC _ON _ELEMENT _NODE)
JPT.Debugger(amt _info)
```
