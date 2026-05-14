---
title: "MeshEdit.RemoveSolidMesh()"
description: "Remove Solid Mesh"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > RemoveSolidMesh"
---

## Description

Remove Solid Mesh

## Syntax

```psj
MeshEdit.RemoveSolidMesh(crlParts=[], bConvFirst=False)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bConvFirst`

- The conv first.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.RemoveSolidMesh(crlParts=[], bConvFirst=False)
```
