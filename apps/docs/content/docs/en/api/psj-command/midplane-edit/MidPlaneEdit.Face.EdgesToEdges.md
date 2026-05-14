---
title: "MidPlaneEdit.Face.EdgesToEdges()"
description: "add face by edges"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlaneEdit > Face > EdgesToEdges"
---

## Description

Add face by edges

## Syntax

```psj
MidPlaneEdit.Face.EdgesToEdges(crlEdges, bImprint=False, bMultiEdges=False)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdges`

- The edge.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bImprint`

- The imprint.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bMultiEdges`

- The multi edges.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Face.EdgesToEdges(crlEdges, bImprint=False, bMultiEdges=False)
```
