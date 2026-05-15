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

<!-- @since:5.0.1 @required -->
### crlNodes

- Specify the node.

<!-- @since:5.0.1 @optional -->
### iTypeEquiva

- Specify the type equiva.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTolerance

- Specify the tolerance.
- The default value is 1.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.Equivalence(crlNodes, iTypeEquiva=0, dTolerance=1.0)
```
