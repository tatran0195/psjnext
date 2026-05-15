---
title: "JPT.GetPostElemFromPosition()"
description: "Get Post Element from Position"
version _introduced: "5.0.1"
available _versions: "all"
---

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

<!-- @since:5.0.1 @required -->
### xCoordValue

- Specify the value in X coordinate in millimeters \[mm] in the Cartesian coordinate system..

<!-- @since:5.0.1 @required -->
### yCoordValue

- Specify the value in Y coordinate in millimeters \[mm] in the Cartesian coordinate system..

<!-- @since:5.0.1 @required -->
### zCoordValue

- Specify the value in Z coordinate in millimeters \[mm] in the Cartesian coordinate system.

<!-- @since:5.0.1 @required -->
### dTolerance

- Specify the tolerance to search the satisfying element in millimeters \[mm]. This argument will help to find the first nearest element with the input position.

<!-- @since:5.0.1 @required -->
### bVisible

- Specify the search mode.
  - _True_: Only search for elements which is displayed on the screen
  - _False_: Enable to search in the hidden elements

## Return Code

A _[DPostElem](../data-type/psj-utility/post-utility/post-built-in-types/DPostElem)_ object containing the Post Element information.

## Sample Code

```psj {15}
JPT.ClearLog()
# Set up model path
JupiterPath = JPT.GetAppPathInfo(JPT.PathType.PROGRAM _PATH)
modelPath = JupiterPath + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"

# Import result
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 1, 1, 1)'.format(modelPath))
JPT.ViewFitToModel()

# Show Result
JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, Mises, 2}, {2, 0, 0, 0, 0, 0, 0, 0.000000, 0}, \
0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
{0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
JPT.Exec('CmdShowPostDeformation(183:1, 1, 0, 1, 1, 0, 0.000000, 0, 0.070000, 0, 0.070000, 0.070000, 0.070000, 0)')

# Get Element by position
elemWith _Tolerance = JPT.GetPostElemFromPosition(16, 20, 5, 0.1, 1)
JPT.Debugger(elemWith _Tolerance) #Element ID = 409
```
