---
title: "MeshEdit.MoveNode.Point()"
description: "Move node(s) to an Face(Edge) Point position"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > Point"
---

## Description

Move node(s) to an Face(Edge) Point position

## Syntax

```psj
MeshEdit.MoveNode.Point(dX=0.0, dY=0.0, dZ=0.0, ilNodeList=[])
```

## Inputs

<!-- @since:5.0.1 @optional -->
### dX

- Specify the x.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dY

- Specify the y.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dZ

- Specify the z.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### ilNodeList

- Specify the node list.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Point(dX=0.0, dY=0.0, dZ=0.0, ilNodeList=[])
```
