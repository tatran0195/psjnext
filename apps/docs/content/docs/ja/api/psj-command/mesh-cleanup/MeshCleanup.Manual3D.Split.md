---
title: "MeshCleanup.Manual3D.Split()"
description: "Merge two Quad elements into one Quad element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual3D > Split"
---

## Description

Merge two Quad elements into one Quad element

## Syntax

```psj
MeshCleanup.Manual3D.Split(crplElemEdge, crlNodes=[], dRatioDistance=0.5)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crplElemEdge

- Specify the element edge.

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dRatioDistance

- Specify the ratio distance.
- The default value is 0.5.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.Split(crplElemEdge, crlNodes=[], dRatioDistance=0.5)
```
