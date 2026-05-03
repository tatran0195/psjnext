---
title: "MeshEdit.MoveNode.ProjectToPlaneElem()"
description: "Move Node by Project to Plane(Elem)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > ProjectToPlaneElem"
---

## Description

Move Node by Project to Plane(Elem)

## Syntax

```psj
MeshEdit.MoveNode.ProjectToPlaneElem(crlNodes=[], crlElems=[])
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

### `crlElems` @type(List\[Cursor]) @default(\[])

- The element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.ProjectToPlaneElem(crlNodes=[], crlElems=[])
```
