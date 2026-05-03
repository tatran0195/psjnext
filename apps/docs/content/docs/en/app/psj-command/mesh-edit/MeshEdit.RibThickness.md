---
title: "MeshEdit.RibThickness()"
description: "Mesh Edit Morphing Rib Thickness"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > RibThickness"
---

## Description

Mesh Edit Morphing Rib Thickness

## Syntax

```psj
MeshEdit.RibThickness(crlFaceMove=[], crlFaceFixed=[], dMove=3.00, dDistStrong=10.00, dDistWeak=20.00)
```

## Inputs

### `crlFaceMove` @type(List\[Cursor]) @default(\[])

- The face move.

### `crlFaceFixed` @type(List\[Cursor]) @default(\[])

- The face fixed.

### `dMove` @type(Double) @default(3.00)

- The move.

### `dDistStrong` @type(Double) @default(10.00)

- The dist strong.

### `dDistWeak` @type(Double) @default(20.00)

- The dist weak.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.RibThickness(crlFaceMove=[], crlFaceFixed=[], dMove=3.00, dDistStrong=10.00, dDistWeak=20.00)
```
