---
title: "JPT.PostHasDeform()"
description: "Check whether if the working result has deformation or not"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Check whether the working result has deformation or not.

## Syntax

```psj
JPT.PostHasDeform(PostAnalysisType,
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

A _Boolean_ specifying the working result has deformation or not.

## Sample Code

```psj {10}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 4}, {1, 1, 0, 0, 1, 8, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                             {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                             {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

bool_check_deform = JPT.PostHasDeform(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC, 1, 1)
JPT.Debugger(bool_check_deform) #True
```
