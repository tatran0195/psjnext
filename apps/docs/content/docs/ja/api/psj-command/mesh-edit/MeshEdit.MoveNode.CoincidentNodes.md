---
title: "MeshEdit.MoveNode.CoincidentNodes()"
description: "Coincident Nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > CoincidentNodes"
---

## Description

Coincident Nodes

## Syntax

```psj
MeshEdit.MoveNode.CoincidentNodes(crlNodes=[], dTol=0.01, bDesOrder=False)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the tolerance.
- The default value is 0.01.

<!-- @since:5.0.1 @optional -->
### bDesOrder

- Specify the des order.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.CoincidentNodes(crlNodes=[], dTol=0.01, bDesOrder=False)
```
