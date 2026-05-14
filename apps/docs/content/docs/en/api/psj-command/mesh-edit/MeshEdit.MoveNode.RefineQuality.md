---
title: "MeshEdit.MoveNode.RefineQuality()"
description: "MeshEdit RefineQuality"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > RefineQuality"
---

## Description

MeshEdit RefineQuality

## Syntax

```psj
MeshEdit.MoveNode.RefineQuality(iMetric=0, crlFaces=[], crlElems=[], crlNodes=[])
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMetric`

- The metric.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlElems`

- The element.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.RefineQuality(iMetric=0, crlFaces=[], crlElems=[], crlNodes=[])
```
