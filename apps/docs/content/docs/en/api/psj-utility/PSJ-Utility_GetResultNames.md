---
title: "JPT.GetResultNames()"
description: "Get all the available result type existing on the model"
version _introduced: "5.0.1"
available _versions: "all"
---

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

<!-- @since:5.0.1 @type:PostAnalysisType @required -->
### `PostAnalysisType`

- The _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.

<!-- @since:5.0.1 @type:Integer @required -->
### `resultSet`

- The step ID of the imported result.

<!-- @since:5.0.1 @type:Integer @required -->
### `timeStep`

- The time step of the imported result.

<!-- @since:5.0.1 @type:BoolType @required -->
### `BoolType`

- The _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ specifying whether to use the name of the current language setting.
  - _True_: Use the name of the current language setting.
  - _False_: Use the English name.

## Return Code

A _List of String_ containing all the available result types existing on the model.

## Sample Code

```psj {5-9}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

#Get All Result Names in all steps and increments
steps=JPT.GetResultSteps()
for step in steps:
    incs=JPT.GetResultIncrements(step.first, step.third)
    for inc in incs:
        result _name = JPT.GetResultNames(step.first,    #analysis type
                                         step.third,    #result set
                                         inc,           #time step
                                         JPT.BoolType.TRUE _VAL)

        JPT.Debugger(result _name)
```
