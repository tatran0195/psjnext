---
title: "JPT.GetResultLocations()"
description: "Get all the available data location existing on the inputted result type and direction"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get all the available data location existing on the inputted result type and direction.

## Syntax

```psj
JPT.GetResultLocations(PostAnalysisType,
                       resultSet,
                       timeStep,
                       resultName,
                       componentName)
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

<!-- @since:5.0.1 @type:String @required -->
### `componentName`

- A specific direction of the result (Such as X, Y, Z, etc.).

## Return Code

A _List of Integer_ containing all the available [PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types) of the inputted result type and it's direction.

## Sample Code

```psj {5-11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result _location = \
    JPT.GetResultLocations(JPT.PostAnalysisType.POST _ANALYSIS _LINEAR _STATIC,
                           1,
                           1,
                           "Stress",
                           "XX")

JPT.Debugger(result _location)
#2: JPT.PostResultDataLoc.POST _LOC _ON _ELEMENT
#4: JPT.PostResultDataLoc.POST _LOC _ON _ELEMENT _NODE
```
