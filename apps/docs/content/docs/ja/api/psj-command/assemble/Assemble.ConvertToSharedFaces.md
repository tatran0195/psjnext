---
title: "Assemble.ConvertToSharedFaces()"
description: "If a pair of Tri elements that share all three vertices exists within the document or on the specified surface, they are converted into a shared surface between the two parts to which they belong."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Assemble > ConvertToSharedFaces"
macro _link: ""
---

## Description

If a pair of Tri elements that share all three vertices exists within the document or on the specified surface, they are converted into a shared surface between the two parts to which they belong.

## Syntax

```psj
Assemble.ConvertToSharedFaces(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### crlFaces

- Specify the target faces. If the list is empty, all faces in the document are considered as targets.
- The default value is \[].

## Return Code

A _List of Cursor_ specifying the created shared face.

## Sample Code

```psj {5}
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=7463537)
MeshEdit.MergeNodes(dTolerance=0.1, iKeepType=2, crlTargets=[Face(49, 24)])

shared _face = Assemble.ConvertToSharedFaces(crlFaces=[Face(24, 49)])
JPT.Debugger(shared _face)
```
