---
title: "MainWindow.RightClick.MergeFaces()"
description: "Merge Faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MainWindow > RightClick > MergeFaces"
---

## Description

Merge Faces

## Syntax

```psj
MainWindow.RightClick.MergeFaces(crlFaces, bIsMergeEdge=False, bRemoveNonBoundEdge=True)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The face.

### `bIsMergeEdge` @type(Boolean) @default(False)

- The is merge edge.

### `bRemoveNonBoundEdge` @type(Boolean) @default(True)

- The remove non boundary edge.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MainWindow.RightClick.MergeFaces(crlFaces, bIsMergeEdge=False, bRemoveNonBoundEdge=True)
```
