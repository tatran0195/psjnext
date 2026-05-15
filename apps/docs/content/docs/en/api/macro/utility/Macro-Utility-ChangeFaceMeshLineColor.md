---
title: "ChangeFaceMeshLineColor()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Change the color of the mesh lines of selected faces.

## Syntax

```psj
ChangeFaceMeshLineColor(Cursor[] Faces, Color Color)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

A cursor list of faces.

<!-- @since:5.1.0 -->
### 2. color

Specify the color of mesh line.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ChangeFaceMeshLineColor([6:21, 6:22, 6:23, 6:24, 6:25, 6:26], 12603648)
```
