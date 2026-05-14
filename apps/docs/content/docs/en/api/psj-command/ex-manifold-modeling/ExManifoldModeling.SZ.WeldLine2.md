---
title: "ExManifoldModeling.SZ.WeldLine2()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "ExManifoldModeling > SZ > WeldLine2"
---

## Description

## Syntax

```psj
ExManifoldModeling.SZ.WeldLine2(crlFaces, crlParts, dLayerWidth, iLayerNumber)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Double @required -->
### `dLayerWidth`

- The layer width.

<!-- @since:5.0.1 @type:Integer @required -->
### `iLayerNumber`

- The layer number.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
ExManifoldModeling.SZ.WeldLine2(crlFaces, crlParts, dLayerWidth, iLayerNumber)
```
