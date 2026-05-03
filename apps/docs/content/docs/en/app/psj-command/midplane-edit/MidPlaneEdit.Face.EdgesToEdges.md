---
title: "MidPlaneEdit.Face.EdgesToEdges()"
description: "add face by edges"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlaneEdit > Face > EdgesToEdges"
---

## Description

Add face by edges

## Syntax

```psj
MidPlaneEdit.Face.EdgesToEdges(crlEdges, bImprint=False, bMultiEdges=False)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @required

- The edge.

### `bImprint` @type(Boolean) @default(False)

- The imprint.

### `bMultiEdges` @type(Boolean) @default(False)

- The multi edges.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Face.EdgesToEdges(crlEdges, bImprint=False, bMultiEdges=False)
```
