---
title: "JPT.GetResultComponentNames()"
description: "Get all the available result direction of the inputted result type"
version _introduced: "5.0.1"
available _versions: "all"
---

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

<!-- @since:5.0.1 @type:PostAnalysisType @required -->
### `PostAnalysisType`

- The _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.

<!-- @since:5.0.1 @type:Integer @required -->
### `resultSet`

- The step ID of the imported result.

<!-- @since:5.0.1 @type:Integer @required -->
### `timeStep`

- The time step of the imported result.

<!-- @since:5.0.1 @type:String @required -->
### `resultName`

- The type of result (Such as Displacement, Stress, etc.).

<!-- @since:5.0.1 @type:BoolType @required -->
### `BoolType`

- The _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection:
  - _True_: Select the inputted entity with its ID.
  - _False_: Deselect the inputted entity with its ID.

## Return Code

A _List of String_ containing all the available data directions of the inputted result type.

## Sample Code

```psj {5-10}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

steps=JPT.GetResultSteps()
for step in steps:
    incs=JPT.GetResultIncrements(step.first, step.third)
    for inc in incs:
        result _comp _name = JPT.GetResultComponentNames(step.first,     # analysis type
                                                       step.third,     # result set
                                                       inc,            # time step
                                                       "Displacement", # result name
                                                       JPT.BoolType.TRUE _VAL)

        JPT.Debugger(result _comp _name)
```
