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

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bConvFirst

- Specify the conv first.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.RemoveSolidMesh(crlParts=[], bConvFirst=False)
```
