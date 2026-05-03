---
title: "MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace()"
description: "project an edge to face to get a new edge"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlaneEdit > AddItems > Edge > ProjectEdgeToFace"
---

## Description

Project an edge to face to get a new edge

## Syntax

```psj
MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace(crlEdges, crlFaces, bExtendEdge=True)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @required

- The edge.

### `crlFaces` @type(List\[Cursor]) @required

- The face.

### `bExtendEdge` @type(Boolean) @default(True)

- The extend edge.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace(crlEdges, crlFaces, bExtendEdge=True)
```
