---
title: "Assemble.SeparateFaces.Solid()"
description: "Separate a shared face between parts into distinct faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assemble > Separate Faces > Solid"
---

## Description

Separate a shared face between parts into distinct faces.

## Syntax

```psj
Assemble.SeparateFaces.Solid(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The target parts which have shared faces between them.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The target shared faces.

### `iCreateGroup` @type(Boolean) @default(0)

- The type of group will be created.

## Return Code

A _List Cursor_ of separated faces if success, or _None_ if fail.

## Sample Code

```psj {9,10}
Geometry.Part.Cube(iPartColor=15658599)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=7961077)
Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[49, 24], 
                        dTolerance=0.001, 
                        iTypeConnectPos=0)

faces = Assemble.SeparateFaces.Solid(crlParts=[Part(1, 2)], 
                                     iCreateGroup=2)
JPT.Debugger(faces)
```
