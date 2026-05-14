---
title: "MeshEdit.DividePartByRegion()"
description: "Divide Part By Region"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > DividePartByRegion"
---

## Description

Divide Part By Region

## Syntax

```psj
MeshEdit.DividePartByRegion(crlParts=[], crlBoundaryParts=[])
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlBoundaryParts`

- The boundary parts.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.DividePartByRegion(crlParts=[], crlBoundaryParts=[])
```
