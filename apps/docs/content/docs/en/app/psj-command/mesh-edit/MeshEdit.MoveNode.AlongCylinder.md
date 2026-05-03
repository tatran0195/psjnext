---
title: "MeshEdit.MoveNode.AlongCylinder()"
description: "Move node along cylinder surface"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > AlongCylinder"
---

## Description

Move node along cylinder surface

## Syntax

```psj
MeshEdit.MoveNode.AlongCylinder(crlFaces=[], crlNodes=[], dIrX=0, dIrY=0, dIrZ=0, dCircleX=0, dCircleY=0, dCircleZ=0, dRadius=0, dHeight=0)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

### `dIrX` @type(Double) @default(0)

- The direction x.

### `dIrY` @type(Double) @default(0)

- The direction y.

### `dIrZ` @type(Double) @default(0)

- The direction z.

### `dCircleX` @type(Double) @default(0)

- The circle x.

### `dCircleY` @type(Double) @default(0)

- The circle y.

### `dCircleZ` @type(Double) @default(0)

- The circle z.

### `dRadius` @type(Double) @default(0)

- The radius.

### `dHeight` @type(Double) @default(0)

- The height.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.AlongCylinder(crlFaces=[], crlNodes=[], dIrX=0, dIrY=0, dIrZ=0, dCircleX=0, dCircleY=0, dCircleZ=0, dRadius=0, dHeight=0)
```
