---
title: "Geometry.Transform.CylinderFace()"
description: "Transform to matching two cylindrical surfaces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Transform > Cylinder Face"
---

## Description

Translate two parts such that the specified two cylindrical surfaces concentric.

## Syntax

```psj
Geometry.Transform.CylinderFace(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The cylinder part.

### `veclPoint` @type(List\[Vector]) @default(\[\[0.0, 0.0, 0.0]])

- The points to define the matching plane from source and target.
  It contains the position of six points, the first three points define the source face, the others define the target face.

### `bCreateNewPart` @type(Boolean) @default(False)

- Whether to keep the original part and create a new part after the transform operation.

### `bCopyLBC` @type(Boolean) @default(False)

- Whether to copy load boundary condition from original part to transformed one.
  This argument will be ignored i&#x66;_&#x62;CreateNewPart=False_.

### `bCopyProperty` @type(Boolean) @default(False)

- Whether to copy property from original part to transformed one.
  This argument will be ignored i&#x66;_&#x62;CreateNewPart=False_.

## Return Code

No return value.

## Sample Code

```psj {3}
Geometry.Part.Cylinder()
Geometry.Part.Cylinder(dlOrigin=[0.02, 0.0, 0.0], strName="Cylinder_2", iPartColor=6812659)
Geometry.Transform.CylinderFace(crlParts=[Part(1), Part(2)], veclPoint=[[0, 0, 0], [0, -1000, 0],
    [10, 0, 0], [0, 10, 0], [0, -990, 0], [10.0, 10, 10]], bCreateNewPart=True)
```
