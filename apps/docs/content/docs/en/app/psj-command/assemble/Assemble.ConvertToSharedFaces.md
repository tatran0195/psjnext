---
title: "Assemble.ConvertToSharedFaces()"
description: "If a pair of Tri elements that share all three vertices exists within the document or on the specified surface, they are converted into a shared surface between the two parts to which they belong."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Assemble > ConvertToSharedFaces"
macro_link: ""
---

## Description

If a pair of Tri elements that share all three vertices exists within the document or on the specified surface, they are converted into a shared surface between the two parts to which they belong.

## Syntax

```psj
Assemble.ConvertToSharedFaces(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The target faces. If the list is empty, all faces in the document are considered as targets.

## Return Code

A _List of Cursor_ specifying the created shared face.

## Sample Code

```psj {5}
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7463537)
MeshEdit.MergeNodes(dTolerance=0.1, iKeepType=2, crlTargets=[Face(49, 24)])

shared_face = Assemble.ConvertToSharedFaces(crlFaces=[Face(24, 49)])
JPT.Debugger(shared_face)
```
