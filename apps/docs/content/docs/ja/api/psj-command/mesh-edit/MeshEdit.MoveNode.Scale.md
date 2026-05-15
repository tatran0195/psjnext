---
title: "MeshEdit.MoveNode.Scale()"
description: "Move node scale"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > Scale"
---

## Description

Move node scale

## Syntax

```psj
MeshEdit.MoveNode.Scale(crlNodes=[], crlNodesOrigin=[], crCoord=None, posDeltaXYZ=[10.0, 10.0, 10.0])
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlNodesOrigin

- Specify the node original.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### posDeltaXYZ

- Specify the delta x y z.
- The default value is \[10.0, 10.0, 10.0].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Scale(crlNodes=[], crlNodesOrigin=[], crCoord=None, posDeltaXYZ=[10.0, 10.0, 10.0])
```
