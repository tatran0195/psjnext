---
title: "JPT.GetResultIncrements()"
description: "Get all the existing increments of the inputted result step"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Get all the existing increments of the inputted result step.

## Syntax

```psj
JPT.GetResultIncrements(PostAnalysisType,
                        resultSet)
```

## Inputs

### `PostAnalysisType` @type(Enum) @required

- Th&#x65;_[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_&#x64;escribing the type of analysis result.

### `resultSet` @type(Integer) @required

- The step ID of the imported result.

## Return Code

A _List of Integer_ containing all the existing increments of the inputted result type with it's step.

## Sample Code

```psj {5-8}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_increments = \
    JPT.GetResultIncrements(JPT.PostAnalysisType.POST_ANALYSIS_MODAL,
                            1)

JPT.Debugger(result_increments)
```
