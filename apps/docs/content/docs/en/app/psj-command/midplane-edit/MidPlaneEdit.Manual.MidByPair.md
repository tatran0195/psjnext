---
title: "MidPlaneEdit.Manual.MidByPair()"
description: "Midplane Manual MidByPair"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlaneEdit > Manual > MidByPair"
---

## Description

Midplane Manual MidByPair

## Syntax

```psj
MidPlaneEdit.Manual.MidByPair(crlBaseFaces, crlPairFaces, crlRefFaces, crPart, bMergeFaces, bExtendFaces, bHideFaces, dExtendTol, dMergeEdgesAngle, dStitchFaces)
```

## Inputs

### `crlBaseFaces` @type(List\[Cursor]) @required

- The base faces.

### `crlPairFaces` @type(List\[Cursor]) @required

- The pair faces.

### `crlRefFaces` @type(List\[Cursor]) @required

- The reference faces.

### `crPart` @type(Cursor) @required

- The part.

### `bMergeFaces` @type(Boolean) @required

- The merge faces.

### `bExtendFaces` @type(Boolean) @required

- The extend faces.

### `bHideFaces` @type(Boolean) @required

- The hide faces.

### `dExtendTol` @type(Double) @required

- The extend tolerance.

### `dMergeEdgesAngle` @type(Double) @required

- The merge edges angle.

### `dStitchFaces` @type(Double) @required

- The stitch faces.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Manual.MidByPair(crlBaseFaces, crlPairFaces, crlRefFaces, crPart, bMergeFaces, bExtendFaces, bHideFaces, dExtendTol, dMergeEdgesAngle, dStitchFaces)
```
