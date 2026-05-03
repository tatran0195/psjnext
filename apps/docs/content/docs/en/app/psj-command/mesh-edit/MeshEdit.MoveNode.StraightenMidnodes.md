---
title: "MeshEdit.MoveNode.StraightenMidnodes()"
description: "move node by straighten_mid_nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > StraightenMidnodes"
---

## Description

Move node by straighten\_mid\_nodes

## Syntax

```psj
MeshEdit.MoveNode.StraightenMidnodes(crlParts=[], crlFaces=[], crlEdges=[], crlNodes=[])
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `crlEdges` @type(List\[Cursor]) @default(\[])

- The edge.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.StraightenMidnodes(crlParts=[], crlFaces=[], crlEdges=[], crlNodes=[])
```
