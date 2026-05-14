---
title: "MuxWeld.MeshingPass()"
description: "sweep cross section to create welding"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MuxWeld > MeshingPass"
---

## Description

Sweep cross section to create welding

## Syntax

```psj
MuxWeld.MeshingPass(crPart=None, crlEdges=[], dMeshSize=0.0)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crPart`

- The part.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlEdges`

- The edge.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMeshSize`

- The mesh size.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.MeshingPass(crPart=None, crlEdges=[], dMeshSize=0.0)
```
