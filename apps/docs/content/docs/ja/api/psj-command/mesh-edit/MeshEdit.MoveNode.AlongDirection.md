---
title: "MeshEdit.MoveNode.AlongDirection()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > AlongDirection"
---

## Description

## Syntax

```psj
MeshEdit.MoveNode.AlongDirection(crlNodes=[], crElem=None, crFace=None, vecDirection=[0,0,0], dMagnitude=0.0, bDestination=False)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crElem

- Specify the element.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crFace

- Specify the face.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### vecDirection

- Specify the direction.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### dMagnitude

- Specify the magnitude.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### bDestination

- Specify the destination.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.AlongDirection(crlNodes=[], crElem=None, crFace=None, vecDirection=[0,0,0], dMagnitude=0.0, bDestination=False)
```
