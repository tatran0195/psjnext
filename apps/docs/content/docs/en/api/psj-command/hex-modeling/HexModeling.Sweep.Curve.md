---
title: "HexModeling.Sweep.Curve()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > Sweep > Curve"
---

## Description

Unknown Description

## Syntax

```psj
HexModeling.Sweep.Curve(crFace=None, crlEdges=[], crlRefEdge=[], dMeshSize=0.1)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crFace`

- The face.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlEdges`

- The edge.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlRefEdge`

- The reference edge.

<!-- @since:5.0.1 @type:Double @optional @default:0.1 -->
### `dMeshSize`

- The mesh size.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
HexModeling.Sweep.Curve(crFace=None, crlEdges=[], crlRefEdge=[], dMeshSize=0.1)
```
