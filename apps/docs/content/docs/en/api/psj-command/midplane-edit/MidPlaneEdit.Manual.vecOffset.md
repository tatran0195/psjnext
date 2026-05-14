---
title: "MidPlaneEdit.Manual.vecOffset()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlaneEdit > Manual > vecOffset"
---

## Description

Unknown Description

## Syntax

```psj
MidPlaneEdit.Manual.vecOffset(crlFaces, crPart, dOffset, bCyl, strNewPartName)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crPart`

- The part.

<!-- @since:5.0.1 @type:Double @required -->
### `dOffset`

- The offset.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bCyl`

- The cylinder.

<!-- @since:5.0.1 @type:String @required -->
### `strNewPartName`

- The new part name.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Manual.vecOffset(crlFaces, crPart, dOffset, bCyl, strNewPartName)
```
