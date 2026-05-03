---
title: "Geometry.BodyCut.XXYYOnOnePoint()"
description: "Separate a part along the specified coordinate plane with one node as a starting point"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Body Cut > XX-YY On 1 Point"
macro_link: "[CutBodyByPlane](../../macro/geometry/CutBodyByPlane)"
---

## Description

Separate a part along the specified coordinate plane with one node as a starting point.

## Syntax

```psj
Geometry.BodyCut.XXYYOnOnePoint(...)
```

## Inputs

### `crPart` @type(Cursor) @required

- The part to partition.

### `posCutPoint` @type(Position) @default(\[0.0,0.0,0.0])

- A point on the cutting plane. This position can get from node, point on edge or point on face.

### `iCuttingPlane` @type(Integer) @default(0)

- The cutting plane.
  - I&#x66;_&#x69;Type = 0_, cutting by plane Oxy.
  - I&#x66;_&#x69;Type = 1_, cutting by plane Oxz.
  - I&#x66;_&#x69;Type = 2_, cutting by plane Oyz.

### `dOffsetDistance` @type(Double) @default(0.0)

- The offset distance from the selected position.

### `bSplitOnly` @type(Boolean) @default(False)

- Whether or not retain the original part.
  - I&#x66;_&#x46;alse_, the specified part will be divided into two parts separately.
  - I&#x66;_&#x54;rue_, the specified part just split by cutting plane without dividing into two parts.

### `bMakeSectionFace` @type(Boolean) @default(True)

- Whether to generate a cross-section face at the division section.

### `bSharedFace` @type(Boolean) @default(False)

- Whether to generate a shared face at the division section. This argument will only affect the functionality whe&#x6E;_&#x62;MakeSectionFace=Tru&#x65;_&#x61;n&#x64;_&#x62;SplitOnly=False_.

### `crLocalCoordinate` @type(Cursor) @default(None)

- The local coordinate. When the default value is used, the global coordinate is selected.

### `bSeparateFace` @type(Boolean) @default(False)

- Whether to prevent the section faces to be coupled (merge) in the enclave. This option will only affect the functionality i&#x66;_&#x62;MakeSectionFace=True_.
  - I&#x66;_&#x54;rue_, the section faces will be created separately.
  - I&#x66;_&#x46;alse_, only a section face will be created.

## Return Code

A _List of Cursor_ specifying the new bodies.

## Sample Code

```psj {3,4,5,6,7,8,9}
Torus = Geometry.Part.Torus(strName="Torus_2", iPartColor=14114775)

separate_status = Geometry.BodyCut.XXYYOnOnePoint(crPart=Torus, 
                                                  posCutPoint=[-0.015,
                                                               -0.005, 
                                                               0.006],
                                                  iCuttingPlane=1, 
                                                  bSharedFace=True, 
                                                  bSeparateFace=True)

JPT.Debugger(separate_status)
```
