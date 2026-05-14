---
title: "MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace()"
description: "project an edge to face to get a new edge"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlaneEdit > AddItems > Edge > ProjectEdgeToFace"
---

## Description

Project an edge to face to get a new edge

## Syntax

```psj
MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace(crlEdges, crlFaces, bExtendEdge=True)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdges`

- The edge.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bExtendEdge`

- The extend edge.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace(crlEdges, crlFaces, bExtendEdge=True)
```
