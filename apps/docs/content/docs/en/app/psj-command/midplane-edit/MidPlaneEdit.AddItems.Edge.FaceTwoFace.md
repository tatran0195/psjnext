---
title: "MidPlaneEdit.AddItems.Edge.FaceTwoFace()"
description: "Exent face to face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlaneEdit > AddItems > Edge > FaceTwoFace"
---

## Description

Exent face to face

## Syntax

```psj
MidPlaneEdit.AddItems.Edge.FaceTwoFace(crRefFace=None, crExtFace=None, iExtendType=0)
```

## Inputs

### `crRefFace` @type(Cursor) @default(None)

- The reference face.

### `crExtFace` @type(Cursor) @default(None)

- The extend face.

### `iExtendType` @type(Integer) @default(0)

- The extend type.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.AddItems.Edge.FaceTwoFace(crRefFace=None, crExtFace=None, iExtendType=0)
```
