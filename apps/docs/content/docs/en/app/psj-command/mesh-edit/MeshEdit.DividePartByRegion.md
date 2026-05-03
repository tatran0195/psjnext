---
title: "MeshEdit.DividePartByRegion()"
description: "Divide Part By Region"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > DividePartByRegion"
---

## Description

Divide Part By Region

## Syntax

```psj
MeshEdit.DividePartByRegion(crlParts=[], crlBoundaryParts=[])
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `crlBoundaryParts` @type(List\[Cursor]) @default(\[])

- The boundary parts.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.DividePartByRegion(crlParts=[], crlBoundaryParts=[])
```
