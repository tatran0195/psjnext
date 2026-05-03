---
title: "MeshEdit.MoveNode.AlongEdge()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > AlongEdge"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description is missing in all versions — placeholder inserted
-->

## Description

## Syntax

```psj
MeshEdit.MoveNode.AlongEdge(crlNodes=[], bMoveX=False, bMoveY=False, bMoveZ=False, dPosX=0.0, dPosY=0.0, dPosZ=0.0, iMoveType=0)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

### `bMoveX` @type(Boolean) @default(False)

- The move x.

### `bMoveY` @type(Boolean) @default(False)

- The move y.

### `bMoveZ` @type(Boolean) @default(False)

- The move z.

### `dPosX` @type(Double) @default(0.0)

- The position x.

### `dPosY` @type(Double) @default(0.0)

- The position y.

### `dPosZ` @type(Double) @default(0.0)

- The position z.

### `iMoveType` @type(Integer) @default(0)

- The move type.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.AlongEdge(crlNodes=[], bMoveX=False, bMoveY=False, bMoveZ=False, dPosX=0.0, dPosY=0.0, dPosZ=0.0, iMoveType=0)
```
