---
title: "JPT.GetResultComponentNames()"
description: "Get all the available result direction of the inputted result type"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Get all the available result directions of the inputted result type.

## Syntax

```psj
JPT.GetResultComponentNames(PostAnalysisType,
                            resultSet,
                            timeStep,
                            resultName,
                            BoolType)
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

### `BoolType` @type(Enum) @required

- Th&#x65;_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_&#x64;escribing the selection:
  - _True_: Select the inputted entity with its ID.
  - _False_: Deselect the inputted entity with its ID.

## Return Code

A _List of String_ containing all the available data directions of the inputted result type.

## Sample Code

```psj {5-10}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

steps=JPT.GetResultSteps()
for step in steps:
    incs=JPT.GetResultIncrements(step.first, step.third)
    for inc in incs:
        result_comp_name = JPT.GetResultComponentNames(step.first,     # analysis type
                                                       step.third,     # result set
                                                       inc,            # time step
                                                       "Displacement", # result name
                                                       JPT.BoolType.TRUE_VAL)

        JPT.Debugger(result_comp_name)
```
