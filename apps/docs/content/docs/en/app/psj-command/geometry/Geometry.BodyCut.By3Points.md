---
title: "Geometry.BodyCut.By3Points()"
description: "Separate a part using the given cutting planes defined by three points to partition the target parts"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Body Cut > 3 Points"
macro_link: "[BodyCutBy3PointsS](../../macro/geometry/BodyCutBy3PointsS)"
---

## Description

Separate a part using the given cutting planes defined by three points to partition the target parts.

## Syntax

```psj
Geometry.BodyCut.By3Points(...)
```

## Inputs

### `crPart` @type(Cursor) @required

- The part to partition.

### `poslPoints` @type(List\[Position]) @default(\[\[0.0,0.0,0.0], \[0.0,0.0,0.0], \[0.0,0.0,0.0]])

- Positions to define the cutting plane. Each position can get from node, point on edge or point on face.

### `dOffsetDistance` @type(Double) @default(0.0)

- The offset distance from the selected positions.

### `bSplitOnly` @type(Boolean) @default(False)

- Whether or not to retain the original part.
  - I&#x66;_&#x46;alse_, the given part will be divided into two parts separately.
  - I&#x66;_&#x54;rue_, the given part just split by cutting plane without dividing into two parts.

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

```psj {3,4,5,6,7,8}
part = Geometry.Part.Torus(strName="Torus_2", iPartColor=14114775)

cutting_status = Geometry.BodyCut.By3Points(crPart=part, 
                                            poslPoints=[[-0.038, -0.019, 0.017],
                                                        [-0.019, -0.010, 0.015], 
                                                        [0.048, 0.022, -0.006]], 
                                            bSharedFace=True, 
                                            bSeparateFace=True)

JPT.Debugger(cutting_status)
```
