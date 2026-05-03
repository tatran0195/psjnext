---
title: "MeshCleanup.Face()"
description: "change topology face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Face"
---

## Description

Change topology face

## Syntax

```psj
MeshCleanup.Face(crlFaces=[], crlParts=[], bCreateNewPart=False)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `bCreateNewPart` @type(Boolean) @default(False)

- The create new part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Face(crlFaces=[], crlParts=[], bCreateNewPart=False)
```
