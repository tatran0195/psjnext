---
title: "MeshEdit.MeshCopy()"
description: "Mesh Copy Pattern"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MeshCopy"
---

## Description

Mesh Copy Pattern

## Syntax

```psj
MeshEdit.MeshCopy(crlFaces=[], crlNodes=[])
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MeshCopy(crlFaces=[], crlNodes=[])
```
