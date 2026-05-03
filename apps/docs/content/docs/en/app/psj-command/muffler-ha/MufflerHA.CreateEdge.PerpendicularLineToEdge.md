---
title: "MufflerHA.CreateEdge.PerpendicularLineToEdge()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MufflerHA > CreateEdge > PerpendicularLineToEdge"
---

## Description

Unknown Description

## Syntax

```psj
MufflerHA.CreateEdge.PerpendicularLineToEdge(crNode, crEdge, crlFaces, bBreakFace)
```

## Inputs

### `crNode` @type(Cursor) @required

- The node.

### `crEdge` @type(Cursor) @required

- The edge.

### `crlFaces` @type(List\[Cursor]) @required

- The face.

### `bBreakFace` @type(Boolean) @required

- The break face.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MufflerHA.CreateEdge.PerpendicularLineToEdge(crNode, crEdge, crlFaces, bBreakFace)
```
