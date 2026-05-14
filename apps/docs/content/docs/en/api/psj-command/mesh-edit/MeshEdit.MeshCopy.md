---
title: "MeshEdit.MeshCopy()"
description: "Mesh Copy Pattern"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MeshCopy"
---

## Description

Mesh Copy Pattern

## Syntax

```psj
MeshEdit.MeshCopy(crlFaces=[], crlNodes=[])
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MeshCopy(crlFaces=[], crlNodes=[])
```
