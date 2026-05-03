---
title: "Tools.DraftAngleShowContour()"
description: "Display result contour of Draft Angle function."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > DraftAngleShowContour"
macro_link: "ShowContourDraftAngle"
---

## Description

Display result contour of Draft Angle function.

## Syntax

```psj
Tools.DraftAngleShowContour(...)
```

## Inputs

### `listPairCursorData` @type(List\[Cursor-Value]) @required

- A list of pair data (list type), which data includes cursor and value.

### `iContourDivision` @type(Integer)

- The number of divisions of contour.

### `dContourMax` @type(Double)

- The number of the maximum value of contour.

### `dContourMin` @type(Double)

- The number of the minimum value of contour.

## Return Code

- A _Boolean_ specifying whether the function succeeded or not.
  - 0: Failed
  - 1: Succeeded

## Sample Code

```psj {31,34-36}
#Create Sample Model
Geometry.Part.Trapezoid(
    dlLength=[0.01, 0.001, 0.01], 
    ilAxialNodes=[10, 2, 10], 
    iPartColor=7961077)

JPT.ViewFitToModel()

MeshEdit.OneNode(
    crlNodes=[Node(45)],
    crlFaceFixed=[Face(21)], 
    bOffsetvector=True, dlOffset=[0.8, 0.0, 0.0], dOffset=0.0, 
    dDistStrong=2.0, dDistWeak=5.0)

MeshEdit.OneNode(
    crlNodes=[Node(56)],
    crlFaceFixed=[Face(21)], 
    bOffsetvector=True, dlOffset=[-0.8, 0.0, 0.0], dOffset=0.0,
    dDistStrong=2.0, dDistWeak=5.0)

MeshEdit.OneNode(
    crlNodes=[Node(4)], 
    crlFaceFixed=[Face(21)], 
    bOffsetvector=True, dlOffset=[0.8, 0.0, 0.0], dOffset=0.0, 
    dDistStrong=2.0, dDistWeak=5.0)

#Calculate Draft Angle
draft_angle_result=Tools.DraftAngle(dlDraftDirection=[0, 1, 0], crlTargets=[Part(1)])

#Show result by contour
Tools.DraftAngleShowContour(listPairCursorData=draft_angle_result)

#Show result with different parameter 
Tools.DraftAngleShowContour(
    listPairCursorData=draft_angle_result, 
    iDivisionNumber=5, dContourMax=60, dContourMin=-60)
```
