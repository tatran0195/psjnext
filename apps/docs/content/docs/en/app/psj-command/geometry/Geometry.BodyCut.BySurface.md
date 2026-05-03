---
title: "Geometry.BodyCut.BySurface()"
description: "Separate a part using the given cutting planes (By selecting face) to partition the target parts"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Body Cut > By Surface"
macro_link: "[BodyCutBySurfaceS](../../macro/geometry/BodyCutBySurfaceS)"
---

## Description

Separate a part using the given cutting planes (By selecting face) to partition the target parts.

## Syntax

```psj
Geometry.BodyCut.BySurface(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The parts to partition.

### `crCutter` @type(Cursor) @required

- The cutting face.

### `bSplitOnly` @type(Boolean) @default(False)

- Whether to prevent split the given part into two separate bodies.
  - I&#x66;_&#x54;rue_, the specified part just split by cut plane without dividing into two parts.
  - I&#x66;_&#x46;alse_, the specified part will be divided into two parts separately.

### `bMakeSectionFace` @type(Boolean) @default(True)

- Whether to generate a cross-section face at the division section.

### `bSharedFace` @type(Boolean) @default(False)

- Whether to generate a shared face at the division section. This argument will only affect the functionality whe&#x6E;_&#x62;MakeSectionFace=Tru&#x65;_&#x61;n&#x64;_&#x62;SplitOnly=False_.

### `bSeparateFace` @type(Boolean) @default(False)

- Whether to prevent the section faces to be coupled (merge) in the enclave. This option will only affect the functionality i&#x66;_&#x62;MakeSectionFace=True_.
  - I&#x66;_&#x54;rue_, the section faces will be created separately.
  - I&#x66;_&#x46;alse_, only a section face will be created.

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

separated_bodies = Geometry.BodyCut.BySurface(crlParts=[Part(1)], 
                                              crCutter=Part(2), 
                                              bSharedFace=True)

JPT.Debugger(separated_bodies)
```
