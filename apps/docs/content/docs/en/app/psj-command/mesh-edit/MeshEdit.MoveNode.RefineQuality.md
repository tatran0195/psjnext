---
title: "MeshEdit.MoveNode.RefineQuality()"
description: "MeshEdit RefineQuality"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > RefineQuality"
---

## Description

MeshEdit RefineQuality

## Syntax

```psj
MeshEdit.MoveNode.RefineQuality(iMetric=0, crlFaces=[], crlElems=[], crlNodes=[])
```

## Inputs

### `iMetric` @type(Integer) @default(0)

- The metric.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `crlElems` @type(List\[Cursor]) @default(\[])

- The element.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.RefineQuality(iMetric=0, crlFaces=[], crlElems=[], crlNodes=[])
```
