---
title: "Geometry.BodyCut.By3Points()"
description: "Separate a part using the given cutting planes defined by three points to partition the target parts"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Body Cut > 3 Points"
macro _link: "[BodyCutBy3PointsS](../../macro/geometry/BodyCutBy3PointsS)"
---

## Description

Separate a part using the given cutting planes defined by three points to partition the target parts.

## Syntax

```psj
Geometry.BodyCut.By3Points(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crPart

- Specify the part to partition.

<!-- @since:5.0.1 @optional -->
### poslPoints

- Specify positions to define the cutting plane. Each position can get from node, point on edge or point on face.
- The default value is \[\[0.0,0.0,0.0], \[0.0,0.0,0.0], \[0.0,0.0,0.0]].

<!-- @since:5.0.1 @optional -->
### dOffsetDistance

- Specify the offset distance from the selected positions.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### bSplitOnly

- Specify whether or not to retain the original part.
  - If _False_, the given part will be divided into two parts separately.
  - If _True_, the given part just split by cutting plane without dividing into two parts.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bMakeSectionFace

- Specify whether to generate a cross-section face at the division section.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bSharedFace

- Specify whether to generate a shared face at the division section. This argument will only affect the functionality when _bMakeSectionFace=True_ and _bSplitOnly=False_.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bSeparateFace

- Specify whether to prevent the section faces to be coupled (merge) in the enclave. This option will only affect the functionality if _bMakeSectionFace=True_.
  - If _True_, the section faces will be created separately.
  - If _False_, only a section face will be created.
- The default value is _False_

## Return Code

A _List of Cursor_ specifying the new bodies.

## Sample Code

```psj {3,4,5,6,7,8}
part = Geometry.Part.Torus(strName="Torus _2", iPartColor=14114775)

cutting _status = Geometry.BodyCut.By3Points(crPart=part, 
                                            poslPoints=[[-0.038, -0.019, 0.017],
                                                        [-0.019, -0.010, 0.015], 
                                                        [0.048, 0.022, -0.006]], 
                                            bSharedFace=True, 
                                            bSeparateFace=True)

JPT.Debugger(cutting _status)
```
