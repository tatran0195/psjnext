---
title: "MeshEdit.MoveNode.StraightenMidnodes()"
description: "move node by straighten _mid _nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > StraightenMidnodes"
---

## Description

Move node by straighten\_mid\_nodes

## Syntax

```psj
MeshEdit.MoveNode.StraightenMidnodes(crlParts=[], crlFaces=[], crlEdges=[], crlNodes=[])
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlEdges`

- The edge.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.StraightenMidnodes(crlParts=[], crlFaces=[], crlEdges=[], crlNodes=[])
```
