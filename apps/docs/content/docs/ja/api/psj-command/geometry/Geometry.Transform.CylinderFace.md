---
title: "Geometry.Transform.CylinderFace()"
description: "Transform to matching two cylindrical surfaces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Transform > Cylinder Face"
---

## Description

Translate two parts such that the specified two cylindrical surfaces concentric.

## Syntax

```psj
Geometry.Transform.CylinderFace(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the cylinder part.

<!-- @since:5.0.1 @optional -->
### veclPoint

- Specify the points to define the matching plane from source and target.
  It contains the position of six points, the first three points define the source face, the others define the target face.
- The default value is \[\[0.0, 0.0, 0.0]].

<!-- @since:5.0.1 @optional -->
### bCreateNewPart

- Specify whether to keep the original part and create a new part after the transform operation.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCopyLBC

- Specify whether to copy load boundary condition from original part to transformed one.
  This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCopyProperty

- Specify whether to copy property from original part to transformed one.
  This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

## Return Code

No return value.

## Sample Code

```psj {3}
Geometry.Part.Cylinder()
Geometry.Part.Cylinder(dlOrigin=[0.02, 0.0, 0.0], strName="Cylinder _2", iPartColor=6812659)
Geometry.Transform.CylinderFace(crlParts=[Part(1), Part(2)], veclPoint=[[0, 0, 0], [0, -1000, 0],
    [10, 0, 0], [0, 10, 0], [0, -990, 0], [10.0, 10, 10]], bCreateNewPart=True)
```
