---
title: "MeshEdit.MoveNode.AlongDirection()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > AlongDirection"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description is missing in all versions — placeholder inserted
-->

## Description

## Syntax

```psj
MeshEdit.MoveNode.AlongDirection(crlNodes=[], crElem=None, crFace=None, vecDirection=[0,0,0], dMagnitude=0.0, bDestination=False)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

### `crElem` @type(Cursor) @default(None)

- The element.

### `crFace` @type(Cursor) @default(None)

- The face.

### `vecDirection` @type(Vector) @default(\[0,0,0])

- The direction.

### `dMagnitude` @type(Double) @default(0.0)

- The magnitude.

### `bDestination` @type(Boolean) @default(False)

- The destination.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.AlongDirection(crlNodes=[], crElem=None, crFace=None, vecDirection=[0,0,0], dMagnitude=0.0, bDestination=False)
```
