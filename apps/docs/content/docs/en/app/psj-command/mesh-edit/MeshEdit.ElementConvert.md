---
title: "MeshEdit.ElementConvert()"
description: "Element Conversion"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > ElementConvert"
---

## Description

Element Conversion

## Syntax

```psj
MeshEdit.ElementConvert(crlParts=[], iType=1)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `iType` @type(Integer) @default(1)

- The type.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.ElementConvert(crlParts=[], iType=1)
```
