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

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlEdges

- Specify the edge.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the node.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.StraightenMidnodes(crlParts=[], crlFaces=[], crlEdges=[], crlNodes=[])
```
