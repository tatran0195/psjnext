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

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the faces.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bMeshCopy

- Specify the mesh copy.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.FaceImprint(crlFaces=[], bMeshCopy=False)
```
