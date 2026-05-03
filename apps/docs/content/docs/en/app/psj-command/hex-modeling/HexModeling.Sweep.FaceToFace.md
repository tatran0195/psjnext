---
title: "HexModeling.Sweep.FaceToFace()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > Sweep > FaceToFace"
---

## Description

Unknown Description

## Syntax

```psj
HexModeling.Sweep.FaceToFace(crSrcFace, crDstFace, bDeleteOriginalParts=True)
```

## Inputs

### `crSrcFace` @type(Cursor) @required

- The source face.

### `crDstFace` @type(Cursor) @required

- The dst face.

### `bDeleteOriginalParts` @type(Boolean) @default(True)

- The delete original parts.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
HexModeling.Sweep.FaceToFace(crSrcFace, crDstFace, bDeleteOriginalParts=True)
```
