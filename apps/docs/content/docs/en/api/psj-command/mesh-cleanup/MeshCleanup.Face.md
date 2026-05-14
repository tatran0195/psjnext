---
title: "MeshCleanup.Face()"
description: "change topology face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Face"
---

## Description

Change topology face

## Syntax

```psj
MeshCleanup.Face(crlFaces=[], crlParts=[], bCreateNewPart=False)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCreateNewPart`

- The create new part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Face(crlFaces=[], crlParts=[], bCreateNewPart=False)
```
