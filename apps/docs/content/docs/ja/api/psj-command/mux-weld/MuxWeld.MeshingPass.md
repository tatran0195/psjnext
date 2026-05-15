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

<!-- @since:5.0.1 @optional -->
### crPart

- Specify the part.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crlEdges

- Specify the edge.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dMeshSize

- Specify the mesh size.
- The default value is 0.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.MeshingPass(crPart=None, crlEdges=[], dMeshSize=0.0)
```
