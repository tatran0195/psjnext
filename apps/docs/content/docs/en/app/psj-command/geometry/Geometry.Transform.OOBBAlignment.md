---
title: "Geometry.Transform.OOBBAlignment()"
description: "A bounding box is defined for each part in such a way that it minimizes empty space, and part movement is performed by aligning these bounding boxes with each other."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Geometry > Transform > OOBBAlignment"
macro_link: "ALIGNMENTBYOOBB"
---

## Description

A bounding box is defined for each part in such a way that it minimizes empty space, and part movement is performed by aligning these bounding boxes with each other.

## Syntax

```psj
Geometry.Transform.OOBBAlignment(...)
```

## Inputs

### `crReferencePart` @type(Cursor) @default(None)

- The target part to which alignment will be made.

### `crMovingPart` @type(Cursor) @default(None)

- The part to be moved.

### `iPositionType` @type(Integer) @default(0)

- The type of alignment.
  - 0: Center of Part
  - 1: Center of Plane1
  - 2: Center of Plane2
  - 3: Center of Plane3
  - 4: Center of Plane4
  - 5: Center of Plane5
  - 6: Center of Plane6
  - 7: Center of Point 1 and 2
  - 8: Center of Point 2 and 3
  - 9: Center of Point 3 and 4
  - 10: Center of Point 4 and 1
  - 11: Center of Point 1 and 5
  - 12: Center of Point 2 and 6
  - 13: Center of Point 3 and 7
  - 14: Center of Point 4 and 8
  - 15: Center of Point 5 and 6
  - 16: Center of Point 6 and 7
  - 17: Center of Point 7 and 8
  - 18: Center of Point 8 and 5
  - 19: Point 1
  - 20: Point 2
  - 21: Point 3
  - 22: Point 4
  - 23: Point 5
  - 24: Point 6
  - 25: Point 7
  - 26: Point 8

### `dlTranslation` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- Trantlation values for adjustment from the moved position.

### `dlRotation` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- Rotation values for adjustment from the moved position.

## Return Code

- A _Boolean_ specifying whether the function successfully executed or not.
  - True: The function successfully executed.
  - False: The function failed.

## Sample Code

```psj{38-43}
#Prepare model

Geometry.Part.Cube(
    dlLength=[0.01, 0.005, 0.003], 
    iPartColor=7697908
)

Geometry.Part.Cube(
    dlLength=[0.008, 0.006, 0.002], 
    strName="Cube_2", 
    iPartColor=7463537
)

Geometry.Transform.Translation(
    crlParts=[Part(2)], 
    dlTranslationVector=[[0.02, 0.005, 0.03]], 
    bCopyReference=True
)

Geometry.Transform.Rotation(
    crlParts=[Part(2)], 
    vecAxis=[0.001, 0.001, 0.001], 
    dAngle=0.523599, 
    dTol=1e-05
)

Geometry.Transform.Rotation(
    crlParts=[Part(2)], 
    posCenter=[0.03143696486949921, 
    0.007476926781237125, 
    0.02508611045777798], 
    vecAxis=[0.001, 0.001, 0.001], 
    dAngle=0.523599, 
    dTol=1e-05
)

# Alignment by OOBB
Geometry.Transform.OOBBAlignment(
    crReferencePart=Part(1), 
    crMovingPart=Part(2), 
    iPositionType=4, 
    dlTranslation=[0, 0.0005, 0]
)

JPT.ViewFitToModel()
```
