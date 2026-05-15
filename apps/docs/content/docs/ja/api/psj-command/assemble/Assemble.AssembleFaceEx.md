---
title: "Assemble.AssembleFaceEx()"
description: "Make assemble faces (shared faces). User inputs the pair faces output from Assemble.FindMatingFaceEx() function, then it will return a list of new shared faces ID created."
version _introduced: "5.0.1"
available _versions: "all"
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

<!-- @since:5.0.1 @required -->
### ilPairFaceToMakeShareFace

- Specify the pair faces to make share face.

<!-- @since:5.0.1 @optional -->
### dTolerance

- Specify the tolerance value.
- The default value is 0.1.

<!-- @since:5.0.1 @optional -->
### iTypeConnectPos

- Specify the type of connect position.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### bFitEdge

- Specify the fit edge option.
- The default value is _False_.

## Return Code

A list of new shared faces ID created.

## Sample Code

```psj {9,10,11,12}
cube1 = Geometry.Part.Cube()
cube2 = Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0], 
                           strName="Cube _2", 
                           iPartColor=6409934)

pair _faces = Assemble.FindMatingFaceEx(crlTaBodies=[cube1, cube2], 
                                       dMatingTol=0.001)

share _faces = Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace = pair _faces, 
                                      dTolerance=0.001,
                                      iTypeConnectPos=0, 
                                      bFitEdge=True)

JPT.Debugger(share _faces)
```
