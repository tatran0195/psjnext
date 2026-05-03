---
title: "JPT.GetResultTimeStepInfo()"
description: "Get the relating information of the inputted result step with it's time step"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Get the relating information of the inputted result step with it's time step.

## Syntax

```psj
JPT.GetResultTimeStepInfo(PostAnalysisType,
                          resultSet,
                          timeStep)
```

## Inputs

### `PostAnalysisType` @type(Enum) @required

- Th&#x65;_[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_&#x64;escribing the type of analysis result.

### `resultSet` @type(Integer) @required

- The step ID of the imported result.

### `timeStep` @type(Integer) @required

- The time step of the imported result.

## Return Code

A _[PostTimeStepInfo](../data-type/psj-utility/post-utility/post-built-in-types/post-time-step-info)_ object specifying the information relating to the inputted time step.

## Sample Code

```psj {5-8}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_time_step_info = JPT.GetResultTimeStepInfo(JPT.PostAnalysisType.POST_ANALYSIS_MODAL,
                                           1,
                                           10)

JPT.Debugger(result_time_step_info)

print(result_time_step_info.mode)
print(result_time_step_info.time)
print(result_time_step_info.freq)
```
