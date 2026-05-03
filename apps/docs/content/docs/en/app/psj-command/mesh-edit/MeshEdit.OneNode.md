---
title: "MeshEdit.OneNode()"
description: "morphing one node"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > OneNode"
---

## Description

Morphing one node

## Syntax

```psj
MeshEdit.OneNode(crlNodes=[], crlFaceFixed=[], bOffsetvector=False, crCoord=None, dlOffset=[0, 1, 0], dOffset=1.0, iDistType=0, dDistStrong=10, dDistWeak=20)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

### `crlFaceFixed` @type(List\[Cursor]) @default(\[])

- The face fixed.

### `bOffsetvector` @type(Boolean) @default(False)

- The offsetvector.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `dlOffset` @type(Double List) @default(\[0, 1, 0])

- The offset.

### `dOffset` @type(Double) @default(1.0)

- The offset.

### `iDistType` @type(Integer) @default(0)

- The dist type.

### `dDistStrong` @type(Double) @default(10)

- The dist strong.

### `dDistWeak` @type(Double) @default(20)

- The dist weak.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.OneNode(crlNodes=[], crlFaceFixed=[], bOffsetvector=False, crCoord=None, dlOffset=[0, 1, 0], dOffset=1.0, iDistType=0, dDistStrong=10, dDistWeak=20)
```
