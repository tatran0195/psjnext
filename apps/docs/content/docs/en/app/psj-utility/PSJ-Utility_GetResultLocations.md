---
title: "JPT.GetResultLocations()"
description: "Get all the available data location existing on the inputted result type and direction"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

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

### `PostAnalysisType` @type(Enum) @required

- Th&#x65;_[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_&#x64;escribing the type of analysis result.

### `resultSet` @type(Integer) @required

- The step ID of the imported result.

### `timeStep` @type(Integer) @required

- The time step of the imported result.

### `resultName` @type(String) @required

- The type of result (Such as Displacement, Stress, etc.).

### `componentName` @type(String) @required

- A specific direction of the result (Such as X, Y, Z, etc.).

## Return Code

A _List of Integer_ containing all the available [PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types) of the inputted result type and it's direction.

## Sample Code

```psj {5-11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_location = \
    JPT.GetResultLocations(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                           1,
                           1,
                           "Stress",
                           "XX")

JPT.Debugger(result_location)
#2: JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT
#4: JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE
```
