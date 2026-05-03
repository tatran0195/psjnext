---
title: "JPT.GetPostElemFromPosition()"
description: "Get Post Element from Position"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Get post element from a specific position.

## Syntax

```psj
JPT.GetPostElemFromPosition(xCoordValue,
                            yCoordValue,
                            zCoordValue,
                            dTolerance,
                            bVisible)
```

## Inputs

### `xCoordValue` @type(Double) @required

- The value in X coordinate in millimeters \[mm] in the Cartesian coordinate system..

### `yCoordValue` @type(Double) @required

- The value in Y coordinate in millimeters \[mm] in the Cartesian coordinate system..

### `zCoordValue` @type(Double) @required

- The value in Z coordinate in millimeters \[mm] in the Cartesian coordinate system.

### `dTolerance` @type(Double) @required

- The tolerance to search the satisfying element in millimeters \[mm]. This argument will help to find the first nearest element with the input position.

### `bVisible` @type(Boolean) @required

- The search mode.
  - _True_: Only search for elements which is displayed on the screen
  - _False_: Enable to search in the hidden elements

## Return Code

A _[DPostElem](../data-type/psj-utility/post-utility/post-built-in-types/DPostElem)_ object containing the Post Element information.

## Sample Code

```psj {15}
JPT.ClearLog()
# Set up model path
JupiterPath = JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH)
modelPath = JupiterPath + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"

# Import result
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 1, 1, 1)'.format(modelPath))
JPT.ViewFitToModel()

# Show Result
JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, Mises, 2}, {2, 0, 0, 0, 0, 0, 0, 0.000000, 0}, \
0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
{0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
JPT.Exec('CmdShowPostDeformation(183:1, 1, 0, 1, 1, 0, 0.000000, 0, 0.070000, 0, 0.070000, 0.070000, 0.070000, 0)')

# Get Element by position
elemWith_Tolerance = JPT.GetPostElemFromPosition(16, 20, 5, 0.1, 1)
JPT.Debugger(elemWith_Tolerance) #Element ID = 409
```
