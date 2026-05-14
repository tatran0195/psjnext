---
title: "MufflerHA.CreateEdge.PerpendicularLineToEdge()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MufflerHA > CreateEdge > PerpendicularLineToEdge"
---

## Description

Unknown Description

## Syntax

```psj
MufflerHA.CreateEdge.PerpendicularLineToEdge(crNode, crEdge, crlFaces, bBreakFace)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @required -->
### `crNode`

- The node.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crEdge`

- The edge.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bBreakFace`

- The break face.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MufflerHA.CreateEdge.PerpendicularLineToEdge(crNode, crEdge, crlFaces, bBreakFace)
```
