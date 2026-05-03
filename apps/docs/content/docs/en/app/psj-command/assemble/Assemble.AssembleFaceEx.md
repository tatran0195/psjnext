---
title: "Assemble.AssembleFaceEx()"
description: "Make assemble faces (shared faces). User inputs the pair faces output from Assemble.FindMatingFaceEx() function, then it will return a list of new shared faces ID created."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assemble > Assemble Faces"
---

## Description

Make assemble faces (shared faces).
User inputs the pair faces output from [Assemble.FindMatingFaceEx()](Assemble.FindMatingFaceEx) function, then it will return a list of new shared faces ID created.

## Syntax

```psj
Assemble.AssembleFaceEx(...)
```

## Inputs

### `ilPairFaceToMakeShareFace` @type(List\[Integer]) @required

- The pair faces to make share face.

### `dTolerance` @type(Double) @default(0.1)

- The tolerance value.

### `iTypeConnectPos` @type(Integer) @default(1)

- The type of connect position.

### `bFitEdge` @type(Boolean) @default(False)

- The fit edge option.

## Return Code

A list of new shared faces ID created.

## Sample Code

```psj {9,10,11,12}
cube1 = Geometry.Part.Cube()
cube2 = Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0], 
                           strName="Cube_2", 
                           iPartColor=6409934)

pair_faces = Assemble.FindMatingFaceEx(crlTaBodies=[cube1, cube2], 
                                       dMatingTol=0.001)

share_faces = Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace = pair_faces, 
                                      dTolerance=0.001,
                                      iTypeConnectPos=0, 
                                      bFitEdge=True)

JPT.Debugger(share_faces)
```
