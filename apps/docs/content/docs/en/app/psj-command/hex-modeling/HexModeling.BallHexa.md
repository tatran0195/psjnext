---
title: "HexModeling.BallHexa()"
description: "hexa modeling ball hexa"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > BallHexa"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Hexa modeling ball hexa

## Syntax

```psj
HexModeling.BallHexa(...)
```

## Inputs

### `crPart` @type(Cursor) @required

- The part.

### `vecCenter` @type(Vector) @default(\[0.0,0.0,0.0])

- The center.

### `dRadius` @type(Double) @default(5.0)

- The radius.

### `dMeshSize` @type(Double) @default(0.5)

- The mesh size.

### `iType` @type(Integer) @default(0)

- The type.

### `iLayer` @type(Integer) @default(3)

- The layer.

### `bMakeCenterNode` @type(Boolean) @default(True)

- The make center node.

### `strName` @type(String) @default("HexBall\_1")

- The part name.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {1-2}
HexModeling.BallHexa(crPart=None, vecCenter=[0.0,0.0,0.0], dRadius=5.0, dMeshSize=0.5, iType=0, 
    iLayer=3, bMakeCenterNode=True, strPartName="HexBall_1")
```
