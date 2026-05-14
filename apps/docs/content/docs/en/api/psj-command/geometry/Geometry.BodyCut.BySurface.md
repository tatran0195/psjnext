---
title: "Geometry.BodyCut.BySurface()"
description: "Separate a part using the given cutting planes (By selecting face) to partition the target parts"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Body Cut > By Surface"
macro _link: "[BodyCutBySurfaceS](../../macro/geometry/BodyCutBySurfaceS)"
---

## Description

Separate a part using the given cutting planes (By selecting face) to partition the target parts.

## Syntax

```psj
Geometry.BodyCut.BySurface(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The parts to partition.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crCutter`

- The cutting face.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSplitOnly`

- Whether to prevent split the given part into two separate bodies.
  - If _True_, the specified part just split by cut plane without dividing into two parts.
  - If _False_, the specified part will be divided into two parts separately.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bMakeSectionFace`

- Whether to generate a cross-section face at the division section.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSharedFace`

- Whether to generate a shared face at the division section. This argument will only affect the functionality when _bMakeSectionFace=True_ and _bSplitOnly=False_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSeparateFace`

- Whether to prevent the section faces to be coupled (merge) in the enclave. This option will only affect the functionality if _bMakeSectionFace=True_.
  - If _True_, the section faces will be created separately.
  - If _False_, only a section face will be created.

## Return Code

A _List of Cursor_ specifying the new bodies.

## Sample Code

```psj {9,10,11}
Geometry.Part.Cube()
Geometry.Part.Cylinder(dlOrigin=[0.005, -0.002, 0.005], 
                       dTopOuterRadius=0.002,
                       dBottomOuterRadius=0.002, 
                       dHeight=0.014)

Geometry.DeleteEntity.Face(crlFaces=[Face(29, 30)])

separated _bodies = Geometry.BodyCut.BySurface(crlParts=[Part(1)], 
                                              crCutter=Part(2), 
                                              bSharedFace=True)

JPT.Debugger(separated _bodies)
```
