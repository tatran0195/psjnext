---
title: "HexModeling.Sweep.FaceToFace()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > Sweep > FaceToFace"
---

## Description

Unknown Description

## Syntax

```psj
HexModeling.Sweep.FaceToFace(crSrcFace, crDstFace, bDeleteOriginalParts=True)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crSrcFace

- Specify the source face.

<!-- @since:5.0.1 @required -->
### crDstFace

- Specify the dst face.

<!-- @since:5.0.1 @optional -->
### bDeleteOriginalParts

- Specify the delete original parts.
- The default value is True.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
HexModeling.Sweep.FaceToFace(crSrcFace, crDstFace, bDeleteOriginalParts=True)
```
