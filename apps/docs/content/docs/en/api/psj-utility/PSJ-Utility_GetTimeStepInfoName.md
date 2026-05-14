---
title: "JPT.GetTimeStepInfoName()"
description: "Get the name of Time Step Info"
version _introduced: "5.0.1"
available _versions: "all"
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

A _String_ specifying the name of Time Step information.

## Sample Code

```psj {5}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

time _step _info _name = JPT.GetTimeStepInfoName(2,1,1)
JPT.Debugger(time _step _info _name) # Mode 1, Freq=3.235953e+04
```
