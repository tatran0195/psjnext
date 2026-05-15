---
title: "MeshCleanup.Manual2D.Split()"
description: "manual cleanup by split"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual2D > Split"
---

## Description

Manual cleanup by split

## Syntax

```psj
MeshCleanup.Manual2D.Split(crplElemEdge, dRatio=0.0, crNodeRef=None, crProjectPart=None)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crplElemEdge

- Specify the element edge.

<!-- @since:5.0.1 @optional -->
### dRatio

- Specify the ratio.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### crNodeRef

- Specify the node reference.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crProjectPart

- Specify the project part.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.Split(crplElemEdge, dRatio=0.0, crNodeRef=None, crProjectPart=None)
```
