---
title: "MainWindow.RightClick.MergeFaces()"
description: "Merge Faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MainWindow > RightClick > MergeFaces"
---

## Description

Merge Faces

## Syntax

```psj
MainWindow.RightClick.MergeFaces(crlFaces, bIsMergeEdge=False, bRemoveNonBoundEdge=True)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the face.

<!-- @since:5.0.1 @optional -->
### bIsMergeEdge

- Specify the is merge edge.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bRemoveNonBoundEdge

- Specify the remove non boundary edge.
- The default value is True.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MainWindow.RightClick.MergeFaces(crlFaces, bIsMergeEdge=False, bRemoveNonBoundEdge=True)
```
