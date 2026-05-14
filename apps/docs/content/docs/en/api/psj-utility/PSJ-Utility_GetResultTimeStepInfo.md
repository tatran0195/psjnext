---
title: "JPT.GetResultTimeStepInfo()"
description: "Get the relating information of the inputted result step with it's time step"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the relating information of the inputted result step with it's time step.

## Syntax

```psj
JPT.GetResultTimeStepInfo(PostAnalysisType,
                          resultSet,
                          timeStep)
```

## Inputs

<!-- @since:5.0.1 @type:PostAnalysisType @required -->
### `PostAnalysisType`

- The _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.

<!-- @since:5.0.1 @type:Integer @required -->
### `resultSet`

- The step ID of the imported result.

<!-- @since:5.0.1 @type:Integer @required -->
### `timeStep`

- The time step of the imported result.

## Return Code

A _[PostTimeStepInfo](../data-type/psj-utility/post-utility/post-built-in-types/post-time-step-info)_ object specifying the information relating to the inputted time step.

## Sample Code

```psj {5-8}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result _time _step _info = JPT.GetResultTimeStepInfo(JPT.PostAnalysisType.POST _ANALYSIS _MODAL,
                                           1,
                                           10)

JPT.Debugger(result _time _step _info)

print(result _time _step _info.mode)
print(result _time _step _info.time)
print(result _time _step _info.freq)
```
