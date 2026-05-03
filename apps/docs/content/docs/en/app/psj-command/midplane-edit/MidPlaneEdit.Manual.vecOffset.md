---
title: "MidPlaneEdit.Manual.vecOffset()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlaneEdit > Manual > vecOffset"
---

## Description

Unknown Description

## Syntax

```psj
MidPlaneEdit.Manual.vecOffset(crlFaces, crPart, dOffset, bCyl, strNewPartName)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The face.

### `crPart` @type(Cursor) @required

- The part.

### `dOffset` @type(Double) @required

- The offset.

### `bCyl` @type(Boolean) @required

- The cylinder.

### `strNewPartName` @type(String) @required

- The new part name.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Manual.vecOffset(crlFaces, crPart, dOffset, bCyl, strNewPartName)
```
