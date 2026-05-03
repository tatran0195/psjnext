---
title: "JPT.GetTimeStepInfoName()"
description: "Get the name of Time Step Info"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get the name of Time Step Info.

## Syntax

```psj
JPT.GetTimeStepInfoName(PostAnalysisType,
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

A _String_ specifying the name of Time Step information.

## Sample Code

```psj {5}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

time_step_info_name = JPT.GetTimeStepInfoName(2,1,1)
JPT.Debugger(time_step_info_name) # Mode 1, Freq=3.235953e+04
```
