---
title: "MeshEdit.RemoveSolidMesh()"
description: "Remove Solid Mesh"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > RemoveSolidMesh"
---

## Description

Remove Solid Mesh

## Syntax

```psj
MeshEdit.RemoveSolidMesh(crlParts=[], bConvFirst=False)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `bConvFirst` @type(Boolean) @default(False)

- The conv first.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.RemoveSolidMesh(crlParts=[], bConvFirst=False)
```
