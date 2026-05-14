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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The starting faces using for the extracting process.

<!-- @since:5.0.1 @type:Double @optional @default:60.0 -->
### `dFaceAngle`

- The limit angle used for spreading from the selected faces to the adjacent faces in degree.
- If _dFaceAngle=-1_, only the selected faces will be extracted.

<!-- @since:5.0.1 @type:String @optional @default:"ExtractFace _1" -->
### `strName`

- The name of the part(s) which will be created after executing the function.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bMergePart`

- Whether to merge the created parts into a single part or not.

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
