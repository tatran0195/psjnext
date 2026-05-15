---
title: "Geometry.ExtractSurfaces()"
description: "Create a new part by recursively finding adjacent surfaces are at an angle of less than or equal to the specified angle"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Extract Surfaces"
---

## Description

Create a new part by recursively finding adjacent surfaces are at an angle of less than or equal to the specified angle.

## Syntax

```psj
Geometry.ExtractSurfaces(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the starting faces using for the extracting process.

<!-- @since:5.0.1 @optional -->
### dFaceAngle

- Specify the limit angle used for spreading from the selected faces to the adjacent faces in degree.
- If _dFaceAngle=-1_, only the selected faces will be extracted.
- The default value is 60.0.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the part(s) which will be created after executing the function.
- The default value is "ExtractFace\_1".

<!-- @since:5.0.1 @optional -->
### bMergePart

- Specify whether to merge the created parts into a single part or not.
- The default value is _False_.

## Return Code

A _List of Cursor_ specifying the created parts.

## Sample Code

```psj {5,6,7,8}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0],
                   strName="Cube _2",
                   iPartColor=6409934)
bodies = Geometry.ExtractSurfaces([Face(52, 26)],
                                  dFaceAngle=-1.0,
                                  strName="ExtractFace _4",
                                  bMergePart=True)
JPT.Debugger(bodies)
```
