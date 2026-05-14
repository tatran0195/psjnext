---
title: "MeshEdit.RefineQuality()"
description: "Resolve poor-quality mesh within the selected face/element/node set by relocating mesh nodes."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > RefineQuality"
---

## Description

Resolve poor-quality mesh within the selected face/element/node set by relocating mesh nodes.

## Syntax

```psj
MeshEdit.RefineQuality(iMetric, crlFaces, crlElems, crlNodes)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @required -->
### `iMetric`

- The metric.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlElems`

- The element.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlNodes`

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.RefineQuality(iMetric, crlFaces, crlElems, crlNodes)
```
