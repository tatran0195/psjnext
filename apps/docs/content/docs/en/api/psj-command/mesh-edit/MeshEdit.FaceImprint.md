---
title: "MeshEdit.FaceImprint()"
description: "import Nastran bdf file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > FaceImprint"
---

## Description

Import Nastran bdf file

## Syntax

```psj
MeshEdit.FaceImprint(crlFaces=[], bMeshCopy=False)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The faces.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bMeshCopy`

- The mesh copy.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.FaceImprint(crlFaces=[], bMeshCopy=False)
```
