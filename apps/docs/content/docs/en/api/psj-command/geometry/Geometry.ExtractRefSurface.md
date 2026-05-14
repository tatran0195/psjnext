---
title: "Geometry.ExtractRefSurface()"
description: "Create a new part by recursively finding adjacent surfaces that are at an angle of less than or equal to the specified angle"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Extract Surfaces"
---

## Description

Create a new part by recursively finding adjacent surfaces that are at an angle of less than or equal to the specified angle.

## Syntax

```psj
Geometry.ExtractRefSurface(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlRefFaces`

- The faces to be extracted.

<!-- @since:5.0.1 @type:Double @optional @default:60.0 -->
### `dFaceAngle`

- The angle in degrees between the adjacent faces to be extracted. If _dFaceAngle=-1_, the selected faces are extracted only.

<!-- @since:5.0.1 @type:String @optional @default:"ExtractFace _1" -->
### `strName`

- The original name of new parts. The final name is a concatenation of the original name and sequence number.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bMergePart`

- Whether to merge new parts into a single part.

## Return Code

A _List of Cursor_ specifying the created parts, or _None_ if fail.

## Sample Code

```psj {13,14,15,16,17}
cube1 = Geometry.Part.Cube()

cube2 = Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0], 
                           strName="Cube _2", 
                           iPartColor=6409934)

Assembly.RightClick.AddToReference(crSrcPart=cube1, 
                                   crDestPart=cube1)

Assembly.RightClick.AddToReference(crSrcPart=cube2, 
                                   crDestPart=cube2)

created _part = Geometry.ExtractRefSurfaces(crlRefFaces=[RefFace((52, 
                                                                 26))], 
                                           dFaceAngle=-1.0, 
                                           strName="ExtractFace _3",
                                           bIsMergePart=True)

JPT.Debugger(created _part)
```
