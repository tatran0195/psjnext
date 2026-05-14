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

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crElem`

- The element.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crFace`

- The face.

<!-- @since:5.0.1 @type:Vector @optional @default:[0,0,0] -->
### `vecDirection`

- The direction.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMagnitude`

- The magnitude.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDestination`

- The destination.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.AlongDirection(crlNodes=[], crElem=None, crFace=None, vecDirection=[0,0,0], dMagnitude=0.0, bDestination=False)
```
