---
title: "MuxWeld.MeshingPass()"
description: "sweep cross section to create welding"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MuxWeld > MeshingPass"
---

## Description

Sweep cross section to create welding

## Syntax

```psj
MuxWeld.MeshingPass(crPart=None, crlEdges=[], dMeshSize=0.0)
```

## Inputs

### `crPart` @type(Cursor) @default(None)

- The part.

### `crlEdges` @type(List\[Cursor]) @default(\[])

- The edge.

### `dMeshSize` @type(Double) @default(0.0)

- The mesh size.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.MeshingPass(crPart=None, crlEdges=[], dMeshSize=0.0)
```
