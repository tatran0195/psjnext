---
title: "Geometry.ExtractSurfaces()"
description: "Create a new part by recursively finding adjacent surfaces are at an angle of less than or equal to the specified angle"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Extract Surfaces"
---

## Description

Create a new part by recursively finding adjacent surfaces are at an angle of less than or equal to the specified angle.

## Syntax

```psj
Geometry.ExtractSurfaces(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The starting faces using for the extracting process.

### `dFaceAngle` @type(Double) @default(60.0)

- The limit angle used for spreading from the selected faces to the adjacent faces in degree.
- I&#x66;_&#x64;FaceAngle=-1_, only the selected faces will be extracted.

### `strName` @type(String) @default("ExtractFace\_1")

- The name of the part(s) which will be created after executing the function.

### `bMergePart` @type(Boolean) @default(False)

- Whether to merge the created parts into a single part or not.

## Return Code

A _List of Cursor_ specifying the created parts.

## Sample Code

```psj {5,6,7,8}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=6409934)
bodies = Geometry.ExtractSurfaces([Face(52, 26)],
                                  dFaceAngle=-1.0,
                                  strName="ExtractFace_4",
                                  bMergePart=True)
JPT.Debugger(bodies)
```
