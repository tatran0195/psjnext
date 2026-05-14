---
title: "MeshCleanup.Manual2D.Equivalence()"
description: "Equivalence Nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual2D > Equivalence"
---

## Description

Equivalence Nodes

## Syntax

```psj
MeshCleanup.Manual2D.Equivalence(crlNodes, iTypeEquiva=0, dTolerance=1.0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iTypeEquiva`

- The type equiva.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dTolerance`

- The tolerance.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.Equivalence(crlNodes, iTypeEquiva=0, dTolerance=1.0)
```
