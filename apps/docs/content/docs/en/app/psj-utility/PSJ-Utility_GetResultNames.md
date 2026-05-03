---
title: "JPT.GetResultNames()"
description: "Get all the available result type existing on the model"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Get all the available result type existing on the model.

## Syntax

```psj
JPT.GetResultNames(PostAnalysisType,
                   resultSet,
                   timeStep,
                   BoolType)
```

## Inputs

### `PostAnalysisType` @type(Enum) @required

- Th&#x65;_[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_&#x64;escribing the type of analysis result.

### `resultSet` @type(Integer) @required

- The step ID of the imported result.

### `timeStep` @type(Integer) @required

- The time step of the imported result.

### `BoolType` @type(Enum) @required

- Th&#x65;_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_&#x73;pecifying whether to use the name of the current language setting.
  - _True_: Use the name of the current language setting.
  - _False_: Use the English name.

## Return Code

A _List of String_ containing all the available result types existing on the model.

## Sample Code

```psj {5-9}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

#Get All Result Names in all steps and increments
steps=JPT.GetResultSteps()
for step in steps:
    incs=JPT.GetResultIncrements(step.first, step.third)
    for inc in incs:
        result_name = JPT.GetResultNames(step.first,    #analysis type
                                         step.third,    #result set
                                         inc,           #time step
                                         JPT.BoolType.TRUE_VAL)

        JPT.Debugger(result_name)
```
