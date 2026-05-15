---
title: "MeshEdit.MoveNode.NormalOffset()"
description: "Move node(s) in Normal Direction of plane"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > NormalOffset"
---

## Description

Move node(s) in Normal Direction of plane

## Syntax

```psj
MeshEdit.MoveNode.NormalOffset(dMagnitude=0.0, ilNodeList=[])
```

## Inputs

<!-- @since:5.0.1 @optional -->
### dMagnitude

- Specify the magnitude.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### ilNodeList

- Specify the node list.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.NormalOffset(dMagnitude=0.0, ilNodeList=[])
```
