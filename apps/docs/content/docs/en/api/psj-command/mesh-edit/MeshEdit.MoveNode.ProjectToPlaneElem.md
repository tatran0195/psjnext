---
title: "MeshEdit.MoveNode.ProjectToPlaneElem()"
description: "Move Node by Project to Plane(Elem)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > ProjectToPlaneElem"
---

## Description

Move Node by Project to Plane(Elem)

## Syntax

```psj
MeshEdit.MoveNode.ProjectToPlaneElem(crlNodes=[], crlElems=[])
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlElems`

- The element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.ProjectToPlaneElem(crlNodes=[], crlElems=[])
```
