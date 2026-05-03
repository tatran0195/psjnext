---
title: "MeshEdit.FaceImprint()"
description: "import Nastran bdf file"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > FaceImprint"
---

## Description

Import Nastran bdf file

## Syntax

```psj
MeshEdit.FaceImprint(crlFaces=[], bMeshCopy=False)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The faces.

### `bMeshCopy` @type(Boolean) @default(False)

- The mesh copy.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.FaceImprint(crlFaces=[], bMeshCopy=False)
```
