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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bIsMergeEdge`

- The is merge edge.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bRemoveNonBoundEdge`

- The remove non boundary edge.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MainWindow.RightClick.MergeFaces(crlFaces, bIsMergeEdge=False, bRemoveNonBoundEdge=True)
```
