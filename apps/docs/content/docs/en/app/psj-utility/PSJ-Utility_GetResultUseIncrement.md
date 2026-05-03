---
title: "JPT.GetResultUseIncrement()"
description: "Check whether the result having any increment or not"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Check whether the result has any increment or not.

## Syntax

```psj
JPT.GetResultUseIncrement(PostAnalysisType,
                          resultSet)
```

## Inputs

### `PostAnalysisType` @type(Enum) @required

- Th&#x65;_[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_&#x64;escribing the type of analysis result.

### `resultSet` @type(Integer) @required

- The step ID of the imported result.

## Return Code

A _Boolean_ specifying the existence of the increment of the inputted time step.

## Sample Code

```psj {5-6}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

is_increment_exist = \
    JPT.GetResultUseIncrement(JPT.PostAnalysisType.POST_ANALYSIS_MODAL, 1)

JPT.Debugger(is_increment_exist)
```
