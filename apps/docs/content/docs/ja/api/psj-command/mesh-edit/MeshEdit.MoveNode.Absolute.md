---
title: "MeshEdit.MoveNode.Absolute()"
description: "move node absolute"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > Absolute"
---

## Description

Move node absolute

## Syntax

```psj
MeshEdit.MoveNode.Absolute(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, b1stCoord=True, b2ndCoord=True, b3rdCoord=True, crlNodes=[], crCoord=None)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### dDeltaX

- Specify the delta x.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dDeltaY

- Specify the delta y.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dDeltaZ

- Specify the delta z.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### b1stCoord

- Specify the coordinate.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### b2ndCoord

- Specify the coordinate.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### b3rdCoord

- Specify the coordinate.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Absolute(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, b1stCoord=True, b2ndCoord=True, b3rdCoord=True, crlNodes=[], crCoord=None)
```
