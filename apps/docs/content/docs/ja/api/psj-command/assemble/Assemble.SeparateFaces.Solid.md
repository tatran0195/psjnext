---
title: "Assemble.SeparateFaces.Solid()"
description: "Separate a shared face between parts into distinct faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assemble > Separate Faces > Solid"
---

## Description

Separate a shared face between parts into distinct faces.

## Syntax

```psj
Assemble.SeparateFaces.Solid(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the target parts which have shared faces between them.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the target shared faces.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iCreateGroup

- Specify the type of group will be created.
- The default value is 0.

## Return Code

A _List Cursor_ of separated faces if success, or _None_ if fail.

## Sample Code

```psj {9,10}
Geometry.Part.Cube(iPartColor=15658599)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=7961077)
Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[49, 24], 
                        dTolerance=0.001, 
                        iTypeConnectPos=0)

faces = Assemble.SeparateFaces.Solid(crlParts=[Part(1, 2)], 
                                     iCreateGroup=2)
JPT.Debugger(faces)
```
