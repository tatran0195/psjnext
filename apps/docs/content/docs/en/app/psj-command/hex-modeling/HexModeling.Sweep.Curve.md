---
title: "HexModeling.Sweep.Curve()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > Sweep > Curve"
---

## Description

Unknown Description

## Syntax

```psj
HexModeling.Sweep.Curve(crFace=None, crlEdges=[], crlRefEdge=[], dMeshSize=0.1)
```

## Inputs

### `crFace` @type(Cursor) @default(None)

- The face.

### `crlEdges` @type(List\[Cursor]) @default(\[])

- The edge.

### `crlRefEdge` @type(List\[Cursor]) @default(\[])

- The reference edge.

### `dMeshSize` @type(Double) @default(0.1)

- The mesh size.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
HexModeling.Sweep.Curve(crFace=None, crlEdges=[], crlRefEdge=[], dMeshSize=0.1)
```
