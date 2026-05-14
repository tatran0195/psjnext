---
title: "Tools.DraftAngle()"
description: "This function measures the draft angle of the mesh in the mold model to verify the draft angle."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > DraftAngle"
macro _link: "DRAFT _ANGLE"
---

## Description

This function measures the draft angle of the mesh in the mold model to verify the draft angle.

## Syntax

```psj
Tools.DraftAngle(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Double] @required -->
### `dlDraftDirection`

- The specifying the draft direction.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The target parts. This is a required input.

## Return Code

<!-- @since:5.1.0 @type:List[Cursor-Value] @optional -->
### `listPairCursorData`

- Which data includes cursor and value.
- Example of return value:
  `[[[11:1], 10], [[11:2], 12]] `
  where \[\[11:1], 10] is Pair Cursor Data including \[11:1] is a cursor, 10 is a value. The first item in Pair Cursor Data is cursor, and the second is a value (could be an integer, double, or a string)

## Sample Code

```psj {28}
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
draft _angle _result=Tools.DraftAngle(dlDraftDirection=[0, 1, 0], crlTargets=[Part(1)])

#Show result by contour
Tools.DraftAngleShowContour(listPairCursorData=draft _angle _result)

#Save result in group 
Tools.DraftAngleCreateGroup(listPairCursorData=draft _angle _result)
```
