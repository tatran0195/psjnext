---
title: "Geometry.ExtractRefSurface()"
description: "Create a new part by recursively finding adjacent surfaces that are at an angle of less than or equal to the specified angle"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Extract Surfaces"
---

## Description

Create a new part by recursively finding adjacent surfaces that are at an angle of less than or equal to the specified angle.

## Syntax

```psj
Geometry.ExtractRefSurface(...)
```

## Inputs

### `crlRefFaces` @type(List\[Cursor]) @required

- The faces to be extracted.

### `dFaceAngle` @type(Double) @default(60.0)

- The angle in degrees between the adjacent faces to be extracted. I&#x66;_&#x64;FaceAngle=-1_, the selected faces are extracted only.

### `strName` @type(String) @default("ExtractFace\_1")

- The original name of new parts. The final name is a concatenation of the original name and sequence number.

### `bMergePart` @type(Boolean) @default(False)

- Whether to merge new parts into a single part.

## Return Code

A _List of Cursor_ specifying the created parts, or _None_ if fail.

## Sample Code

```psj {13,14,15,16,17}
cube1 = Geometry.Part.Cube()

cube2 = Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0], 
                           strName="Cube_2", 
                           iPartColor=6409934)

Assembly.RightClick.AddToReference(crSrcPart=cube1, 
                                   crDestPart=cube1)

Assembly.RightClick.AddToReference(crSrcPart=cube2, 
                                   crDestPart=cube2)

created_part = Geometry.ExtractRefSurfaces(crlRefFaces=[RefFace((52, 
                                                                 26))], 
                                           dFaceAngle=-1.0, 
                                           strName="ExtractFace_3",
                                           bIsMergePart=True)

JPT.Debugger(created_part)
```
