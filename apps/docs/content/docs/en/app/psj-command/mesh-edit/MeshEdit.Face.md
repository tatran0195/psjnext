---
title: "MeshEdit.Face()"
description: "Make Mesh deformation"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > Face"
---

## Description

Make Mesh deformation

## Syntax

```psj
MeshEdit.Face(crlFaces, crlFaceFixed, iOffsetType=0, crCoord=None, dlOffset=[1.0, 0.0, 0.0], dOffset=0, iDistType=0, dDistStrong=10, dDistWeak=20, iNodeIdPick=-1, dlPickForMacro=[])
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The face.

### `crlFaceFixed` @type(List\[Cursor]) @required

- The face fixed.

### `iOffsetType` @type(Integer) @default(0)

- The offset type.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `dlOffset` @type(Double List) @default(\[1.0, 0.0, 0.0])

- The offset.

### `dOffset` @type(Double) @default(0)

- The offset.

### `iDistType` @type(Integer) @default(0)

- The dist type.

### `dDistStrong` @type(Double) @default(10)

- The dist strong.

### `dDistWeak` @type(Double) @default(20)

- The dist weak.

### `iNodeIdPick` @type(Integer) @default(-1)

- The node ID pick.

### `dlPickForMacro` @type(Double List) @default(\[])

- The pick for macro.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.Face(crlFaces, crlFaceFixed, iOffsetType=0, crCoord=None, dlOffset=[1.0, 0.0, 0.0], dOffset=0, iDistType=0, dDistStrong=10, dDistWeak=20, iNodeIdPick=-1, dlPickForMacro=[])
```
