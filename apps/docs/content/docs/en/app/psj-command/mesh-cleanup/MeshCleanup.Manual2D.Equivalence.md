---
title: "MeshCleanup.Manual2D.Equivalence()"
description: "Equivalence Nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Manual2D > Equivalence"
---

## Description

Equivalence Nodes

## Syntax

```psj
MeshCleanup.Manual2D.Equivalence(crlNodes, iTypeEquiva=0, dTolerance=1.0)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @required

- The node.

### `iTypeEquiva` @type(Integer) @default(0)

- The type equiva.

### `dTolerance` @type(Double) @default(1.0)

- The tolerance.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.Equivalence(crlNodes, iTypeEquiva=0, dTolerance=1.0)
```
