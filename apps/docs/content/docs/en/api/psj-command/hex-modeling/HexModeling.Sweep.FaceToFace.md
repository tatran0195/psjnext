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

<!-- @since:5.0.1 @type:Cursor @required -->
### `crSrcFace`

- The source face.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crDstFace`

- The dst face.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bDeleteOriginalParts`

- The delete original parts.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
HexModeling.Sweep.FaceToFace(crSrcFace, crDstFace, bDeleteOriginalParts=True)
```
