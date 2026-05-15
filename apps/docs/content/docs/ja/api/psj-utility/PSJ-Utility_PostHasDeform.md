---
title: "JPT.PostHasDeform()"
description: "Check whether if the working result has deformation or not"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Check whether the working result has deformation or not.

## Syntax

```psj
JPT.PostHasDeform(PostAnalysisType,
                  resultSet,
                  timeStep)
```

## Inputs

<!-- @since:5.0.1 @required -->
### PostAnalysisType

- Specify the_[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.

<!-- @since:5.0.1 @required -->
### resultSet

- Specify the step ID of the imported result.

<!-- @since:5.0.1 @required -->
### timeStep

- Specify the time step of the imported result.

## Return Code

A _Boolean_ specifying the working result has deformation or not.

## Sample Code

```psj {10}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 4}, {1, 1, 0, 0, 1, 8, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                             {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                             {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

bool _check _deform = JPT.PostHasDeform(JPT.PostAnalysisType.POST _ANALYSIS _LINEAR _STATIC, 1, 1)
JPT.Debugger(bool _check _deform) #True
```
