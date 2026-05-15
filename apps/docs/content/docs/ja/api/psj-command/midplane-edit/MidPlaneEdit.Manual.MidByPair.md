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

<!-- @since:5.0.1 @required -->
### crlBaseFaces

- Specify the base faces.

<!-- @since:5.0.1 @required -->
### crlPairFaces

- Specify the pair faces.

<!-- @since:5.0.1 @required -->
### crlRefFaces

- Specify the reference faces.

<!-- @since:5.0.1 @required -->
### crPart

- Specify the part.

<!-- @since:5.0.1 @required -->
### bMergeFaces

- Specify the merge faces.

<!-- @since:5.0.1 @required -->
### bExtendFaces

- Specify the extend faces.

<!-- @since:5.0.1 @required -->
### bHideFaces

- Specify the hide faces.

<!-- @since:5.0.1 @required -->
### dExtendTol

- Specify the extend tolerance.

<!-- @since:5.0.1 @required -->
### dMergeEdgesAngle

- Specify the merge edges angle.

<!-- @since:5.0.1 @required -->
### dStitchFaces

- Specify the stitch faces.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Manual.MidByPair(crlBaseFaces, crlPairFaces, crlRefFaces, crPart, bMergeFaces, bExtendFaces, bHideFaces, dExtendTol, dMergeEdgesAngle, dStitchFaces)
```
