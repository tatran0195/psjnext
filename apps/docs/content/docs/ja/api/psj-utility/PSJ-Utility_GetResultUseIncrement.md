---
title: "JPT.GetResultUseIncrement()"
description: "Check whether the result having any increment or not"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Check whether the result has any increment or not.

## Syntax

```psj
JPT.GetResultUseIncrement(PostAnalysisType,
                          resultSet)
```

## Inputs

<!-- @since:5.0.1 @required -->
### PostAnalysisType

- Specify the_[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.

<!-- @since:5.0.1 @required -->
### resultSet

- Specify the step ID of the imported result.

## Return Code

A _Boolean_ specifying the existence of the increment of the inputted time step.

## Sample Code

```psj {5-6}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

is _increment _exist = \
    JPT.GetResultUseIncrement(JPT.PostAnalysisType.POST _ANALYSIS _MODAL, 1)

JPT.Debugger(is _increment _exist)
```
