---
title: "MidPlaneEdit.AddItems.Edge.FaceTwoFace()"
description: "Exent face to face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlaneEdit > AddItems > Edge > FaceTwoFace"
---

## Description

Exent face to face

## Syntax

```psj
MidPlaneEdit.AddItems.Edge.FaceTwoFace(crRefFace=None, crExtFace=None, iExtendType=0)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crRefFace`

- The reference face.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crExtFace`

- The extend face.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iExtendType`

- The extend type.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.AddItems.Edge.FaceTwoFace(crRefFace=None, crExtFace=None, iExtendType=0)
```
