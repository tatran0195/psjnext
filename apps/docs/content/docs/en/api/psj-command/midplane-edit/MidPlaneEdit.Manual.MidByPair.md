---
title: "MidPlaneEdit.Manual.MidByPair()"
description: "Midplane Manual MidByPair"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlaneEdit > Manual > MidByPair"
---

## Description

Midplane Manual MidByPair

## Syntax

```psj
MidPlaneEdit.Manual.MidByPair(crlBaseFaces, crlPairFaces, crlRefFaces, crPart, bMergeFaces, bExtendFaces, bHideFaces, dExtendTol, dMergeEdgesAngle, dStitchFaces)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlBaseFaces`

- The base faces.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlPairFaces`

- The pair faces.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlRefFaces`

- The reference faces.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crPart`

- The part.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bMergeFaces`

- The merge faces.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bExtendFaces`

- The extend faces.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bHideFaces`

- The hide faces.

<!-- @since:5.0.1 @type:Double @required -->
### `dExtendTol`

- The extend tolerance.

<!-- @since:5.0.1 @type:Double @required -->
### `dMergeEdgesAngle`

- The merge edges angle.

<!-- @since:5.0.1 @type:Double @required -->
### `dStitchFaces`

- The stitch faces.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Manual.MidByPair(crlBaseFaces, crlPairFaces, crlRefFaces, crPart, bMergeFaces, bExtendFaces, bHideFaces, dExtendTol, dMergeEdgesAngle, dStitchFaces)
```
